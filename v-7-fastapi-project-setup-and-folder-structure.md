# Video 7: FastAPI Project Setup and Folder Structure

## 1. Project Overview

In this video, I started setting up a Task Management application using FastAPI.

I created a separate project folder, set up a Python virtual environment, installed FastAPI and Uvicorn, and created the initial folder structure for the application.

## 2. Create the Project Folder

I created a new project folder named `task_management_app` inside the `Learning-FastAPI` repository.

This keeps the Task Management application separate from the earlier FastAPI tutorial examples.

## 3. Set Up the Virtual Environment

I created a Python virtual environment named `env` inside the project.

```powershell
python -m venv env
```

To activate the environment in Windows PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

The virtual environment keeps the project's Python dependencies separate from other projects.

## 4. Install FastAPI and Uvicorn

I installed FastAPI and Uvicorn in the activated virtual environment.

```powershell
python -m pip install fastapi uvicorn
```

* **FastAPI** is used to build the API.
* **Uvicorn** runs the FastAPI application as an ASGI server.

I also created a `requirements.txt` file to record the project's installed dependencies and versions.

## 5. Initialize the Application

I created `main.py` in the project root and initialized the FastAPI application.

```python
from fastapi import FastAPI

app = FastAPI(title="Task Management Application")
```

The `FastAPI()` function creates the application instance.

The `title` parameter sets the application's title, which appears in the API documentation.

At this stage, I initialized the application. Task and user functionality will be added as I continue with the tutorial.

## 6. Project Folder Structure

I created a `src` folder to organize the application's code into separate modules.

```text
task_management_app/
├── main.py
├── requirements.txt
└── src/
    ├── tasks/
    │   ├── __init__.py
    │   ├── controller.py
    │   ├── dtos.py
    │   ├── models.py
    │   └── router.py
    ├── user/
    │   ├── __init__.py
    │   ├── controller.py
    │   ├── dtos.py
    │   ├── models.py
    │   └── router.py
    └── utils/
        ├── __init__.py
        ├── constants.py
        ├── db.py
        └── helpers.py
```

The virtual environment and local `.env` file are kept locally and are not committed to GitHub.

## 7. Purpose of the Folders and Files

### main.py

This is the application's entry point. It contains the FastAPI application instance.

### src/tasks/

This folder organizes files related to task functionality.

* `controller.py` — handles task-related application logic.
* `dtos.py` — defines task data transfer objects.
* `models.py` — contains task data models.
* `router.py` — organizes task-related API routes.
* `__init__.py` — makes the directory a Python package.

### src/user/

This folder organizes files related to user functionality.

* `controller.py` — handles user-related application logic.
* `dtos.py` — defines user data transfer objects.
* `models.py` — contains user data models.
* `router.py` — organizes user-related API routes.
* `__init__.py` — makes the directory a Python package.

### src/utils/

This folder contains shared utility files.

* `constants.py` — stores application constants.
* `db.py` — contains database-related utilities.
* `helpers.py` — contains reusable helper functions.
* `__init__.py` — makes the directory a Python package.

These files provide the initial project structure. Their functionality will be implemented as the tutorial progresses.

## 8. Run and Test the Application

I started the FastAPI application using Uvicorn.

```powershell
python -m uvicorn main:app --reload
```

The `--reload` option automatically restarts the development server when code changes are detected.

I opened the Swagger UI documentation in the browser:

`http://127.0.0.1:8000/docs`

This confirmed that the initial FastAPI application could run.

## 9. Configuration and Git

The `.env` file is intended for local configuration values and should not be committed to GitHub.

The root `.gitignore` file excludes virtual environment folders, Python cache files, and local environment files.

The `requirements.txt` file records the Python dependencies needed to set up the project.

## 10. What I Practiced

* Creating a new FastAPI project.
* Creating and activating a Python virtual environment.
* Installing FastAPI and Uvicorn.
* Initializing a FastAPI application in `main.py`.
* Organizing code into task, user, and utility modules.
* Understanding the purpose of controllers, DTOs, models, routers, and utility files.
* Running the application and opening Swagger UI.
* Keeping local configuration and virtual environment files out of Git.
