# Vidya - The Learning Documentation Platform

**Vidya** is a powerful and user-friendly web application designed for learners to document and track their learning journey in a structured, topic-wise manner. Whether you're studying for exams, learning a new skill, or exploring a subject of interest, Vidya lets you record your progress, take detailed notes, and access your learning anytime, anywhere. 

The platform also allows users to register, login, and manage their personal learning data, ensuring each user’s progress is private and secure.

## Key Features

- **User Authentication**: Sign up, log in, and securely manage your account.
- **Topic-Wise Documentation**: Document your learning by adding topics and detailed entries.
- **Future Access to Learning Entries**: Once you log in, you can access, update, and review your previously saved entries.
- **Responsive User Interface**: Built with HTML, CSS, and JavaScript, providing an intuitive and interactive experience on both desktop and mobile devices.
- **SQLite Database**: The project uses Django's built-in SQLite database to store user and topic data securely.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Full Stack Django)
- **Database**: SQLite (built-in with Django for storing user and topic data)
- **Hosting/Deployment**: PythonAnywhere (Free for the first 3 months)
- **Server**: PythonAnywhere hosting

## Live Demo

The project is **live** and hosted on https://vidyanote.pythonanywhere.com/. You can explore the application and try out its features.

[**Visit the live site**]

## How to Set Up the Project Locally

Follow these easy steps to set up and run the Vidya project on your local machine:

### Step 1: Clone the repository

Start by cloning the project to your local machine using the command:

```bash
git clone git clone https://github.com/keshu-bara/Vidya.git
```

### Step 2: Navigate to the project directory
Once you've cloned the repository, move into the project folder:

```bash
cd Vidya
```

### Step 3: Set up a virtual environment
Create a virtual environment to isolate the project dependencies:

```bash
python -m venv venv
```
Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

For Mac/Linux:
```bash
source venv/bin/activate
```
### Step 4: Install required dependencies
Install Django and other necessary packages using:

```bash
pip install -r requirements.txt
```

### Step 5: Apply Database Migrations
Run the following command to set up the database:

```bash
python manage.py migrate
```
This will create the necessary tables in the SQLite database to store user and topic data.

### Step 6: Create a Superuser (Admin) Account
To create an admin account that allows you to manage the application, run:

```bash
python manage.py createsuperuser
```
Follow the prompts to create a username, email, and password.

### Step 7: Run the Development Server
Now, you're ready to run the server:

```bash
python manage.py runserver
```
The application will be available at http://127.0.0.1:8000/. Open this URL in your browser to start using Vidya locally.

### Step 8: Access and Use the Application

Register: Sign up for an account on the platform.
Login: Once registered, log in to access your learning documentation.
Add Topics: Create topics for different subjects or skills you're learning.
Add Entries: Write detailed notes and track your progress for each topic.
View and Update Entries: After logging in, you can view, edit, or delete your previously saved entries.




