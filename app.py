# Import required modules
from flask import Flask, render_template, request, url_for, redirect, session
from pymongo import MongoClient
from bson.objectid import ObjectId

# Create a new Flask app instance
app = Flask(__name__)
app.secret_key = 'patatita5287'

# Connect to the MongoDB database and set up collections
client = MongoClient('localhost', 27017)
db = client.flask_db
todos = db.todos
users = db.users

# Define a route for the hello world
@app.route('/hello')
def hello():
    return 'Hello, World!'


# Define a route for registering a new user
@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        # Get the user's information from the form
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if the username already exists in the database
        if users.find_one({'username': username}):
            error = 'Username already exists'
        # Check if the password and confirm password match
        elif password != confirm_password:
            error = 'Passwords do not match'
        else:
            # Insert the user's information into the database
            users.insert_one({'username': username, 'password': password})
            return redirect(url_for('login'))

        # Display the registration form with an error message
        return render_template('register.html', error=error)

    # Display the registration form
    return render_template('register.html')

# Define a route for the login page
@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.find_one({'username': username, 'password': password})
        if user:
            session['user_id'] = str(user['_id'])
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html', error=None)

# Define a route for logging out
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# Define a function to get the current user ID
def get_user_id():
    user_id = session.get('user_id', None)
    return ObjectId(user_id) if user_id else None

# Define a route for the home page ('/') with support for GET and POST methods
@app.route('/', methods=('GET', 'POST'))
def index():
    # Redirect to the login page if the user is not authenticated
    if not get_user_id():
        return redirect(url_for('login'))

    # If a POST request is received, add a new to do item to the collection and redirect to the home page
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree, 'user_id': get_user_id()})
        return redirect(url_for('index'))

    # Get the degree parameter from the query string, defaulting to None
    degree = request.args.get('degree')

   # Get to do items from the collection based on the degree parameter
    if degree == 'important':
        all_todos = todos.find({'degree': 'Important'}).sort([('degree', -1), ('_id', -1)])
    elif degree == 'unimportant':
        all_todos = todos.find({'degree': 'Unimportant'}).sort([('degree', -1), ('_id', -1)])
    else:
        all_todos = todos.find().sort([('degree', 1), ('_id', -1)])# Show important tasks on top and then unimportant ones

    return render_template('index.html', todos=all_todos, degree=degree)

# Define a route for creating a new task
@app.route('/create', methods=('GET', 'POST'))
def create():
    # If a POST request is received, add a new to do item to the collection and redirect to the home page
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    return render_template('create.html')

# Define a route for deleting a to do item with a specific ID
@app.post('/<id>/delete/')
def delete(id):
    # Delete the to do item with the specified ID from the collection and redirect to the home page
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

# Define a route for editing a to do item with a specific ID
@app.route('/<id>/edit', methods=('GET', 'POST'))
def edit(id):
    # Find the to do item with the specified ID from the collection
    todo = todos.find_one({"_id": ObjectId(id)})

    # If a POST request is received, update the to do item in the collection and redirect to the home page
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.update_one({"_id": ObjectId(id)}, {"$set": {"content": content, "degree": degree}})
        return redirect(url_for('index'))

    # Display the edit form for the to do item
    return render_template('edit.html', todo=todo)


# Run the app if this file is being executed directly
if __name__ == '__main__':
    app.run(debug=True)