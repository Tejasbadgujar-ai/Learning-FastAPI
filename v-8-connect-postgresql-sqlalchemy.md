# Connect PostgreSQL Database with FastAPI using SQLAlchemy

## 1. Introduction

In this video, I learned how to connect a PostgreSQL database with FastAPI using SQLAlchemy.

SQLAlchemy is a Python library that helps applications communicate with databases.

## 2. What I Learned

* How to connect PostgreSQL with FastAPI.
* How to use SQLAlchemy.
* How to create a database engine.
* How to create database sessions.
* How to use Pydantic Settings.
* How to read database configuration from a `.env` file.
* How to create database tables using SQLAlchemy.

## 3. Files Created

### settings.py

* Imported `BaseSettings` and `SettingsConfigDict` from Pydantic Settings.
* Configured the `.env` file.
* Defined `DB_CONNECTION` to store the database connection URL.
* Created a settings object.

### db.py

* Imported `create_engine` from SQLAlchemy.
* Created a declarative Base.
* Created a database engine using the PostgreSQL connection URL.
* Used `sessionmaker()` to create database sessions.
* Created a `get_db()` function to provide and close database sessions.

### main.py

* Imported FastAPI.
* Imported `Base` and `engine` from the database module.
* Used `Base.metadata.create_all(engine)` to create registered database tables.
* Created the FastAPI application.

## 4. Important Concepts

**create_engine():** Creates a SQLAlchemy engine for database communication.

**declarative_base():** Creates a base class for defining database models.

**sessionmaker():** Creates a factory for database sessions.

**get_db():** Provides a database session and closes it after use.

**Base.metadata.create_all(engine):** Creates database tables for models registered with Base.

**.env:** Stores environment variables such as the database connection URL.

## 5. Testing

Started the FastAPI development server using:

```bash
uvicorn main:app --reload
```

Successfully started the FastAPI application after configuring the PostgreSQL database connection.

## 6. Conclusion

In this video, I learned how to configure PostgreSQL with FastAPI using SQLAlchemy and how to manage database connections and sessions.
