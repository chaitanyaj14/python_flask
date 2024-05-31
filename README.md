# Flask Web Development (Work In Progress)

This project demonstrates my journey in learning Flask, a micro web framework for Python. The developed website showcases essential web development functionalities, including database CRUD operations, pagination, authentication, and deployment.

## Features

### 1. Database CRUD Operations
- **Create**: Forms to input and add new records to the database.
- **Read**: Display records from the database on web pages.
- **Update**: Edit existing records through forms.
- **Delete**: Remove records from the database.

<!-- **Tools Used**: SQLAlchemy for ORM with a SQLite database. -->

### 2. Pagination
- Integrated pagination to manage and display large sets of data efficiently.
- Split data into manageable pages, enhancing user experience.

### 3. Authentication
- User authentication to secure parts of the website.
- User registration, login, and logout functionalities.
- Managed user sessions and authentication processes using Flask-Login.

### 4. Deployment
- Deployed the application to a web server, making it accessible online.
- Used platforms like Heroku for deployment.
- Configured environment variables and database connections for deployment.

## Technologies and Tools
- **Flask**: The primary web framework.
- **SQLAlchemy**: For database interactions.
- **Flask-Login**: For managing user authentication.
<!-- - **Jinja2**: For templating and rendering HTML.
- **Bootstrap**: For front-end styling and responsive design. -->
- **Heroku**: For deployment.

## Learning Outcomes
- Hands-on experience with Flask and its capabilities.
- Understanding of web development concepts such as CRUD operations, pagination, and authentication.
- Knowledge of deploying a web application, managing dependencies, and configuring a production environment.
- Enhanced problem-solving skills through debugging and troubleshooting.

## Getting Started

### Prerequisites
- Python 3.x
- Pip (Python package installer)
- Virtualenv (recommended)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/chaitanyaj14/python_flask.git
    cd python_flask
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

### Running the Application
```bash
flask run
```
The application will be available at `http://127.0.0.1:5000/`.

### Deployment
To deploy the application, you can use platforms like Heroku. Ensure to configure environment variables and database connections as required.
