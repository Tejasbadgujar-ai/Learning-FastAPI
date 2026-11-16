# Video 24 – Background Tasks in FastAPI

## What I Learned

In this video, I learned how to use BackgroundTasks in FastAPI to send emails without making the user wait for the email process to finish.

Normally, sending an email can take around 10–12 seconds. To avoid this delay, I implemented background email sending during user registration.

## 1. Import BackgroundTasks

File: `src/user/router.py`

```python
from fastapi import APIRouter, Depends, Request, BackgroundTasks
```

File: `src/user/controller.py`

```python
from fastapi import Depends, HTTPException, Request, BackgroundTasks
```

I imported BackgroundTasks in both files so I could pass it from the router to the controller.

## 2. Updated Register Route

File: `src/user/router.py`

```python
@user_routes.post("/register", response_model=UserResponseSchema, status_code=201)
async def register(body: UserSchema, bg_task: BackgroundTasks, db: Session = Depends(get_db)):
    return await controller.register(body, db, bg_task)
```

I added `bg_task: BackgroundTasks` to the register endpoint and passed it to the controller.

## 3. Added Background Email Task

File: `src/user/controller.py`

```python
# Send Mail Confirmation
bg_task.add_task(send_email, new_user.email)
```

I used `add_task()` to schedule the email function in the background.

- `send_email` is the function that sends the email.
- `new_user.email` is passed as an argument.
- The email task runs after the response is sent to the client.

This way, the user does not need to wait for the email process to finish.

## 4. Updated Email Function

File: `src/utils/mail.py`

I changed the return message to a print statement for testing:

```python
print({"message": "email has been sent Successfully"})
```

This helped me verify background task execution through the terminal.

## 5. Testing in Postman

I tested the registration endpoint using Postman.

- Sent a POST request to `/user/register`.
- Provided the required user registration details.
- Received a successful registration response.
- Checked the terminal and confirmed that the background task executed.
- The terminal displayed the email confirmation message.

## What I Understood

- I learned how BackgroundTasks work in FastAPI.
- I learned how to pass BackgroundTasks from router to controller.
- I used `add_task()` to execute the email function in the background.
- I understood how background tasks help avoid making users wait for email processing.
- I tested the implementation using Postman and checked the terminal output.

## Conclusion

I successfully implemented background email processing during user registration using FastAPI BackgroundTasks. This helps return the response to the client without waiting for the email process to complete.
