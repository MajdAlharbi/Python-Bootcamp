import os
import re
import subprocess
import sys


# This also runs on macOS, Linux and WSL.
IS_WINDOWS = os.name == "nt"
BIN_DIR = "Scripts" if IS_WINDOWS else "bin"
PYTHON_EXE = "python.exe" if IS_WINDOWS else "python"

VALID_NAME = re.compile(r"^[a-z_][a-z0-9_]*$")


# ------------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------------


def fail(message):
    """Print a clear error and stop with a non-zero exit code."""
    print(f"\nERROR: {message}\n")
    sys.exit(1)


def run(description, command, cwd=None):
    """Run a command and stop if it fails."""
    print(description)

    try:
        subprocess.run(command, cwd=cwd, check=True)

    except subprocess.CalledProcessError as error:
        fail(f"{description.strip()} failed (exit code {error.returncode}).")

    except FileNotFoundError:
        fail(f"Could not find the program: {command[0]}")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def patch(path, old, new, what):
    """Replace text in a file and confirm the replacement happened."""

    with open(path, encoding="utf-8") as handle:
        content = handle.read()

    if old not in content:
        fail(f"Could not patch {what}. Expected to find:\n    {old}")

    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content.replace(old, new, 1))


# ------------------------------------------------------------------
# 1. Inputs
# ------------------------------------------------------------------

folder_name = input("Enter the existing day folder name (e.g. Day-02): ").strip()

if not folder_name:
    fail("The day folder name cannot be empty.")

if not os.path.isdir(folder_name):
    fail(f"The folder '{folder_name}' does not exist here. Create it first.")


project_name = input("Enter the Django project name (e.g. mysite): ").strip()

if not VALID_NAME.match(project_name):
    fail(
        f"'{project_name}' is not a valid project name. "
        "Use lowercase letters, digits and underscores, "
        "and do not start with a digit."
    )


app_names = []

apps_input = input("Enter app names, comma separated (e.g. home,accounts): ")

for raw in apps_input.split(","):
    name = raw.strip()

    if not name:
        continue

    if not VALID_NAME.match(name):
        fail(
            f"'{name}' is not a valid app name. "
            "Use lowercase letters, digits and underscores, "
            "and do not start with a digit."
        )

    if name == project_name:
        fail(f"An app cannot share the project name '{project_name}'.")

    if name not in app_names:
        app_names.append(name)


if not app_names:
    fail("You need at least one app.")


# ------------------------------------------------------------------
# 2. Confirm from the user
# ------------------------------------------------------------------

lab_path = os.path.abspath(os.path.join(folder_name, "lab"))

project_path = os.path.join(lab_path, project_name)


print(f"\nProject  : {project_name}")
print(f"Apps     : {', '.join(app_names)}")
print(f"Location : {project_path}\n")


confirm = input("Create this? (y/n): ").strip().lower()

if confirm != "y":
    print("Cancelled. Nothing was created.")
    sys.exit(0)


if os.path.exists(project_path):
    fail(f"That project folder already exists:\n{project_path}")


# ------------------------------------------------------------------
# 3. Virtual environment
# ------------------------------------------------------------------

os.makedirs(lab_path, exist_ok=True)


venv_path = os.path.join(lab_path, "venv")

venv_python = os.path.join(venv_path, BIN_DIR, PYTHON_EXE)


if os.path.exists(venv_python):
    print("[1/6] Reusing the virtual environment already in 'lab'.")

else:
    run(
        "[1/6] Creating the virtual environment...",
        [
            sys.executable,
            "-m",
            "venv",
            venv_path,
        ],
    )

    if not os.path.exists(venv_python):
        fail(f"venv finished but python was not found at:\n{venv_python}")


# ------------------------------------------------------------------
# 4. Django, project and apps
# ------------------------------------------------------------------

run(
    "[2/6] Upgrading pip...",
    [
        venv_python,
        "-m",
        "pip",
        "install",
        "--upgrade",
        "pip",
        "--quiet",
    ],
)


run(
    "[3/6] Installing Django...",
    [
        venv_python,
        "-m",
        "pip",
        "install",
        "django",
        "--quiet",
    ],
)


run(
    f"[4/6] Creating the project '{project_name}'...",
    [
        venv_python,
        "-m",
        "django",
        "startproject",
        project_name,
    ],
    cwd=lab_path,
)


for app in app_names:
    run(
        f"      Creating the app '{app}'...",
        [
            venv_python,
            "manage.py",
            "startapp",
            app,
        ],
        cwd=project_path,
    )


# ------------------------------------------------------------------
# 5. Wiring
# ------------------------------------------------------------------

print("[5/6] Wiring settings.py and urls.py...")


# ------------------------------------------------------------------
# settings.py
# ------------------------------------------------------------------

settings_file = os.path.join(
    project_path,
    project_name,
    "settings.py",
)


with open(
    settings_file,
    "r",
    encoding="utf-8",
) as handle:
    content = handle.read()


# -----------------------------
# Add apps to INSTALLED_APPS
# -----------------------------

apps_to_add = "".join(f"    '{app}',\n" for app in app_names)


pattern = (
    r"(INSTALLED_APPS\s*=\s*\[\s*)"
    r"(.*?)"
    r"(\n\])"
)


match = re.search(
    pattern,
    content,
    flags=re.DOTALL,
)


if not match:
    fail("Could not find INSTALLED_APPS in settings.py")


new_installed_apps = (
    match.group(1) + match.group(2) + "\n" + apps_to_add.rstrip() + match.group(3)
)


content = content[: match.start()] + new_installed_apps + content[match.end() :]


# -----------------------------
# Add templates directory
# -----------------------------

content, count = re.subn(
    r"""(["']DIRS["']\s*:\s*)\[\]""",
    r"\1[BASE_DIR / 'templates']",
    content,
    count=1,
)


if count == 0:
    fail("Could not patch TEMPLATES DIRS.")


# -----------------------------
# Save settings.py
# -----------------------------

with open(
    settings_file,
    "w",
    encoding="utf-8",
) as handle:
    handle.write(content)


# -----------------------------
# Add static + allowed hosts
# -----------------------------

with open(
    settings_file,
    "a",
    encoding="utf-8",
) as handle:
    handle.write("\nSTATICFILES_DIRS = [\n    BASE_DIR / 'static',\n]\n")

    handle.write("\nALLOWED_HOSTS = ['127.0.0.1', 'localhost']\n")


# ------------------------------------------------------------------
# Main urls.py
# ------------------------------------------------------------------

urls_file = os.path.join(
    project_path,
    project_name,
    "urls.py",
)

with open(urls_file, "r", encoding="utf-8") as handle:
    urls_content = handle.read()


# Add include to import
urls_content, count = re.subn(
    r"from django\.urls import path",
    "from django.urls import include, path",
    urls_content,
    count=1,
)

if count == 0:
    fail("Could not patch the django.urls import in urls.py")


# Build app routes
routes = "".join(f'    path("{app}/", include("{app}.urls")),\n' for app in app_names)


# Add routes after admin route
pattern = r'(\s*path\(["\']admin/["\'],\s*admin\.site\.urls\),)'

match = re.search(pattern, urls_content)

if not match:
    fail("Could not find the admin route in urls.py")


replacement = match.group(1) + "\n" + routes.rstrip()

urls_content = urls_content[: match.start()] + replacement + urls_content[match.end() :]


with open(urls_file, "w", encoding="utf-8") as handle:
    handle.write(urls_content)


# ------------------------------------------------------------------
# App urls.py
# ------------------------------------------------------------------

APP_URLS = """from django.urls import path

from . import views


app_name = "__APP__"


urlpatterns = [
    path("", views.index, name="index"),
]
"""


# ------------------------------------------------------------------
# App views.py
# ------------------------------------------------------------------

APP_VIEWS = """from django.http import HttpResponse


def index(request):
    return HttpResponse("__APP__ is wired up.")
"""


for app in app_names:
    # urls.py
    write(
        os.path.join(
            project_path,
            app,
            "urls.py",
        ),
        APP_URLS.replace(
            "__APP__",
            app,
        ),
    )

    # views.py
    write(
        os.path.join(
            project_path,
            app,
            "views.py",
        ),
        APP_VIEWS.replace(
            "__APP__",
            app,
        ),
    )

    # app/templates/app/
    os.makedirs(
        os.path.join(
            project_path,
            app,
            "templates",
            app,
        ),
        exist_ok=True,
    )


# ------------------------------------------------------------------
# Global templates and static folders
# ------------------------------------------------------------------

os.makedirs(
    os.path.join(
        project_path,
        "templates",
    ),
    exist_ok=True,
)


os.makedirs(
    os.path.join(
        project_path,
        "static",
        "css",
    ),
    exist_ok=True,
)


# ------------------------------------------------------------------
# .gitignore
# ------------------------------------------------------------------

write(
    os.path.join(
        project_path,
        ".gitignore",
    ),
    (
        "venv/\n"
        "__pycache__/\n"
        "*.pyc\n"
        "\n"
        "db.sqlite3\n"
        "\n"
        ".env\n"
        "\n"
        ".vscode/\n"
        ".idea/\n"
        "\n"
        ".DS_Store\n"
        "Thumbs.db\n"
    ),
)


# ------------------------------------------------------------------
# 6. Migrate and freeze
# ------------------------------------------------------------------

run(
    "[6/6] Running migrations...",
    [
        venv_python,
        "manage.py",
        "migrate",
        "--verbosity",
        "0",
    ],
    cwd=project_path,
)


frozen = subprocess.run(
    [
        venv_python,
        "-m",
        "pip",
        "freeze",
    ],
    cwd=project_path,
    capture_output=True,
    text=True,
)


if frozen.returncode != 0:
    fail("pip freeze failed.")


write(
    os.path.join(
        project_path,
        "requirements.txt",
    ),
    frozen.stdout,
)


# ------------------------------------------------------------------
# 7. Print what to run next
# ------------------------------------------------------------------

if IS_WINDOWS:
    activate = os.path.join(
        "venv",
        BIN_DIR,
        "Activate.ps1",
    )

else:
    activate = "source " + os.path.join(
        "venv",
        BIN_DIR,
        "activate",
    )


print(f"\nDone. Project created at:\n{project_path}\n")


print("Next steps, from the 'lab' folder:")


print(f"  cd {os.path.join(folder_name, 'lab')}")


print(f"  {activate}")


print(f"  cd {project_name}")


print("  python manage.py runserver")


print()


print(f"Then open:\nhttp://127.0.0.1:8000/{app_names[0]}/")


print()


print(f"You should see:\n{app_names[0]} is wired up.")
