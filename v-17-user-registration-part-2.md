# 17. User Registration Part 2 - Advanced Validation & Error Handling

## What I Learned

In this video, I continued working on the existing user registration functionality. I learned how to add advanced validation, handle duplicate username and email errors, and update the response schema.

I made the following changes:

## 1. Models (`models.py`)

I corrected the `unique` constraint in the existing UserModel.

```python
username = Column(String, nullable=False, unique=True)
```

### Explanation

- `unique=True` ensures that every username in the database is different.
- It prevents duplicate usernames from being stored in the database.
- I corrected the spelling mistake from `unoque=True` to `unique=True`.

## 2. DTOs (`dtos.py`)

I updated the existing `UserResponseSchema` by adding the `hash_password` field.

```python
class UserResponseSchema(BaseModel):
    name: str
    username: str
    email: str
    mobile_num: str
    id: int
    hash_password: str
```

### Explanation

- `UserResponseSchema` defines the structure of the response returned by the registration API.
- I added `hash_password: str` The hash is not returned in the response, for security.
- The field type `str` indicates that the hash password value must be a string.

## 3. Username Validation (`controller.py`)

I added validation to check whether the username already exists.

```python
is_user = db.query(UserModel).filter(UserModel.username == body.username).first()

if is_user:
    raise HTTPException(status_code=400, detail="Username already exist..")
```

### Explanation

- `db.query(UserModel)` starts a query on the user table.
- `.filter()` applies a condition to search for a matching username.
- `UserModel.username == body.username` compares the database username with the username provided by the user.
- `.first()` returns the first matching record or `None`.
- If a user already exists, `HTTPException` raises a 400 Bad Request error.
- The `detail` parameter sends an error message explaining the problem.

## 4. Email Validation (`controller.py`)

I also added validation to check whether the email address already exists.

```python
is_user = db.query(UserModel).filter(UserModel.email == body.email).first()

if is_user:
    raise HTTPException(status_code=400, detail="Email already exists")
```

### Explanation

- This query checks the email address in the database.
- `UserModel.email == body.email` compares the existing email with the new registration email.
- `.first()` checks whether a matching record is available.
- If the email already exists, the API raises a 400 Bad Request error.
- This prevents users from registering with an already registered email address.

## 5. Postman Testing

I tested the validation functionality using Postman.

- Tested registration with valid user details.
- Tested duplicate username validation.
- Received `400 Bad Request` when using an existing username.
- Tested duplicate email validation.
- Checked the registration response after adding `hash_password` to 
- The hash is not returned in the response, for security.

During today's implementation and testing, I corrected:

- `unoque=True` to `unique=True` in the UserModel.
- Corrected the email validation query to use `UserModel.email` instead of checking the username again.
- Corrected the `HTTPExeption` spelling to `HTTPException`.
- Corrected the JSON request formatting issue that caused the `Extra data` error.

## Conclusion

In this video, I learned how to implement duplicate username and email validation using SQLAlchemy queries. I also understood how `HTTPException` handles validation errors and how to update a Pydantic response schema with additional fields.

### Password Hashing

Password hashing is an important part of user registration.

- `PasswordHash.recommended()` creates a password hashing instance using recommended hashing algorithms, including Argon2.
- Argon2 securely hashes passwords.
- We should never store plain-text passwords in the database because it can expose users' passwords if the database is compromised.
- Instead, we store the hashed password in the database.

**Code:**

```python
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def get_password_hash(password):
    return password_hash.hash(password)
```
