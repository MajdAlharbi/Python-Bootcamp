python --version

mkdir 6rd_P
cd 6rd_P

Set-Content main.py "def main():
    print('Hello')
main()"

Get-Content main.py

python main.py

Set-Content main.py "num = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
print(num + num2)"


python main.py

python -m venv venv

.\venv\Scripts\Activate.ps1

pip install flake8

flake8 --version

pip freeze > requirements.txt

deactivate