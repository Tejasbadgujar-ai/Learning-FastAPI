# Learning FastAPI

This repository contains my FastAPI learning projects and code from tutorial videos.

## Completed Videos

* Video 1
* Video 2
* Video 3
* Video 4
* Video 5
* Video 6

## How to Run the Project

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
uvicorn main:app --reload
```

## API Documentation

After starting the application, open:

http://127.0.0.1:8000/docs




### Video 7+: Task Management App

The Task Management application is located in the `task_management_app/` folder.

### Run the Application

Open a terminal in the project root and run:

```powershell
cd task_management_app
python -m venv env
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Open the API documentation:

http://127.0.0.1:8000/docs

The application's code and dependencies are maintained separately from the FastAPI examples in the repository root.
