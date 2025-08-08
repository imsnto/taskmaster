# TaskMaster

TaskMaster is a personal task management web application built with Django. It allows users to register, log in, and manage tasks with features like creating, viewing, updating, deleting, and filtering tasks by completion status and priority. 

## Features
- User authentication (register, login, logout)
- Task management (create, read, update, delete)
- Task filtering by completion status (All, Completed, Pending) and priority (Low, Medium, High)
- Overdue task highlighting in red

## Requirements
- Python 3.12
- Django 5.2.5

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/imsnto/taskmaster.git
   cd taskmaster

2. **Create and activate a virtual environment**:
    ```bash 
    uv venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **Install dependencies**:
    ```bash
    uv sync # or uv pip install -r requirements.txt

4. **Apply migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Create a superuser (optional, for admin access)**:
    ```bash
    python manage.py createsuperuser

6. **Run the development server**:
    ```bash
    python manage.py runserver

7. **Access the application:**:
    - Open http://127.0.0.1:8000 in your browser.
    - Use /admin for the admin panel (with superuser credentials).
    - Log in or register to manage tasks at /tasks/.


## Project Structure
```
taskmaster/
├── accounts/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── taskmaster/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── settings.py
│   ├── urls.py
├── tasks/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── templates/
├── docs/
├── README.md
├── manage.py
├── .gitignore
├── .python-version
├── db.sqlite3
├── LICENSE
├── requirements.txt
├── uv.lock
```

## Screenshots
Below are screenshots showcasing the app's key functionalities:

- **Task List**:
  ![Task List Page](/docs/_list.png)

- **Create Task**:
  ![Create Task Page](/docs/_creaet.png)

- **Task Update**:  
  ![Task Update Page](/docs/_update.png)

- **Delete Task**:  
  ![Delete Task](/docs/_delete.png)

- **Login Page**:  
  ![Login](/docs/_login.png)

- **Register Page**:
  ![Register](/docs/_register.png_)