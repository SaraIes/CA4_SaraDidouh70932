# CA4_SaraDidouh70932

Flask Task Manager

This is a Flask-based web application allows registered users to create to-do lists. 
As a user, you can see all the listed tasks. First, the important ones are displayed and at the end the unimportant ones are shown. You can also filter according to whether you want to see all tasks, only the important ones, or only the unimportant ones.

It uses MongoDB as the database and includes features for user registration, login, logout, task creation, editing, and deletion. The app includes several routes, defined by their respective URL paths, which are discussed below.

The first route /hello simply displays "Hello, World!" when it is visited.

The default route leads to the main application but if the user in not logged in then it takes them to the login page. /login provides a login form and allows a registered user to login. If the session is successful, it redirects to the home page, otherwise, it shows an error message. If a user is already logged in, it redirects to the home page.
https://github.com/SaraIes/CA4_SaraDidouh70932/blob/main/assets/login.PNG

The third route /register allows a user to register a new account. You can navigate to the registration page trough the login page. The route checks if the entered username already exists in the database and if the password and confirm password fields match before inserting the data. If the registration is successful, it redirects to the login page.
https://github.com/SaraIes/CA4_SaraDidouh70932/blob/main/assets/registration.PNG

The fourth route /logout logs out a user by deleting the session information and redirecting to the login page.

The fifth route '/' is the home page that displays the list of to-do items.
https://github.com/SaraIes/CA4_SaraDidouh70932/blob/main/assets/task-manager.PNG
It shows all the tasks and the degree parameter can be set to 'important' or 'unimportant' to filter the to-do items by their degree of importance. Example filtering only important ones:
https://github.com/SaraIes/CA4_SaraDidouh70932/blob/main/assets/filter-important.PNG

If no degree is specified, the app shows all to-do items sorted by their degree. The user can create and edit the tasks from this. They can also delete them once finished. Confirmation message for deleting:
https://github.com/SaraIes/CA4_SaraDidouh70932/blob/main/assets/delete-task-confirmation.PNG

The sixth route /create provides a form to create a new to-do item. It inserts the new item into the database and redirects to the home page.
https://github.com/SaraIes/CA4_SaraDidouh70932/blob/main/assets/create-task.PNG

In conclusion, this Flask-based web application provides a simple yet efficient to-do list system for registered users. It includes features such as user registration, login, logout, task creation, editing, and deletion. The app is a great example of how Flask and MongoDB can be used to build web applications.
