# Video 23 – How to Send Emails in FastAPI - Complete Email Setup Guide

## Overview

In this video, I learned how to send registration confirmation emails using FastAPI-Mail and Gmail SMTP.

The main objective was to configure email settings, create an email-sending function, and integrate it with the user registration process.

## 1. Required Imports

File: `src/utils/mail.py`

```python
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List
```

**Explanation:**
- `FastMail` is used to send emails.
- `MessageSchema` creates email messages.
- `ConnectionConfig` configures SMTP settings.
- `MessageType` defines the email content type.
- `List` is used for type hints.

## 2. Gmail SMTP Configuration

```python
conf = ConnectionConfig(
    MAIL_USERNAME="your_gmail@gmail.com",
    MAIL_PASSWORD="your_app_password",
    MAIL_FROM="your_gmail@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="TechSimPlus Learnings",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)
```

**Explanation:**
- `MAIL_USERNAME` and `MAIL_PASSWORD` provide Gmail authentication.
- `MAIL_FROM` specifies the sender email.
- `MAIL_PORT` and `MAIL_SERVER` configure Gmail SMTP.
- `MAIL_FROM_NAME` sets the sender's display name.
- `MAIL_STARTTLS` enables secure communication.
- `USE_CREDENTIALS` enables authentication.
- `VALIDATE_CERTS` validates server certificates.

## 3. Creating the send_email() Function

```python
async def send_email(emails: List[str]):
    html = """<p>Hi, Thanks For Registration. Our team Will Connect You</p>"""

    message = MessageSchema(
        subject="Registration Confirmation",
        recipients=emails,
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)

    return {"message": "email has been sent Successfully"}
```

**Explanation:**
- The function accepts recipient email addresses.
- `MessageSchema` prepares the email subject, recipients, and HTML body.
- `FastMail(conf)` initializes the email service.
- `await fm.send_message(message)` sends the email asynchronously.
- Returns a success message.

## 4. Updating User Controller

File: `src/user/controller.py`

First, I changed the existing register function to an asynchronous function.

```python
async def register(body: UserSchema, db: Session):
```

**Explanation:**
- Changed `def register()` to `async def register()` to support asynchronous email sending.

After successfully creating and saving the user, I added:

```python
## Send Mail Confirmation
res = await send_email([new_user.email])
print(res)

return new_user
```

**Explanation:**
- `new_user.email` gets the registered user's email address.
- `await send_email()` sends the confirmation email.
- `print(res)` displays the result.
- `return new_user` returns the registered user.

## 5. Updating User Router

File: `src/user/router.py`

```python
@user_routes.post(
    "/register",
    response_model=UserResponseSchema,
    status_code=201
)
async def register(body: UserSchema, db: Session = Depends(get_db)):
    return await controller.register(body, db)
```

**Explanation:**
- Changed the register endpoint to `async def`.
- `Depends(get_db)` provides the database session.
- `await controller.register(body, db)` calls the asynchronous controller function.
- Returns the registration response.

## 6. Testing Using Postman

I tested the registration functionality using Postman.

**Testing Steps:**

1. Sent a POST request to `/user/register`.
2. Provided the required user registration details.
3. Verified that the user was saved in the database.
4. Checked the registered user's email inbox.
5. Successfully received the registration confirmation email.

## 7. Important Learning

- Learned Gmail SMTP configuration.
- Learned FastAPI-Mail integration.
- Learned to create and send HTML emails.
- Practiced asynchronous functions using `async` and `await`.
- Integrated email confirmation into user registration.
- Tested email functionality using Postman.

## Conclusion

Video 23 is completed.

I successfully integrated FastAPI-Mail with the user registration process. After successful registration, the application sends a confirmation email to the registered user's email address.
