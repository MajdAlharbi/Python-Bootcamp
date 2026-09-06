# Accounts Lab

This lab is a simple Django project to practice working with Views, GET and POST requests, sessions, templates, URLs, and JSON responses.

## What I Practiced

- Creating `Class-Based Views`
- Handling `GET` and `POST`
- Reading form data using `request.POST`
- Saving and reading data from `session`
- Using `render()` and `redirect()`
- Returning a `JsonResponse`
- Connecting views with named URLs
- Using templates for Register, Login, and Profile pages

## Extra Practice

I added a small extra feature to understand the login flow better.

After registration, the username and password are saved in the session.

When the user tries to log in:

- If the username and password are correct, the user is redirected to the Profile page.
- If the login information is incorrect, an error message is shown.
- If the user tries to open the Profile page without logging in, they are redirected to the Login page.

This extra part helped me understand how a website can check whether a user is registered and logged in before allowing access to a page.

> Note: This is only for learning sessions and request handling. In a real Django project, authentication should use Django's built-in authentication system and database instead of storing passwords in sessions.