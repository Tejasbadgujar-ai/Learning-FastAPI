# FastAPI Authentication & Authorization – JWT & Security Guide

## What I Learned

In this video, I learned the basic concepts of Authentication, Authorization and JWT (JSON Web Token) in FastAPI.

### 1. Authentication

Authentication is the process of verifying a user's identity.

For example, when a user logs in using a username and password, the system checks whether the provided credentials are correct.

### 2. Authorization

Authorization determines whether an authenticated user has permission to access a particular resource or perform an action.

### 3. JWT (JSON Web Token)

JWT stands for JSON Web Token.

It is a token used to identify an authenticated user when making API requests.

Instead of sending the username and password with every request, the client sends the generated JWT token.

### 4. Registration Process

During registration, the application collects user information such as:

- Username
- Hashed Password
- Email
- Name
- Mobile Number

The password should be stored in hashed form for security.

### 5. Login Process

The login process generally works as follows:

1. The user enters their username and password.
2. The system validates the username.
3. The system verifies the password.
4. If the credentials are correct, a JWT token is generated.
5. The token is returned to the client.

### 6. JWT Token in API Requests

When a user wants to access a protected API endpoint, the client sends the JWT token with the API request.

The API validates the token before allowing the request.

For example, when creating a task, the API checks whether the user has a valid token.

### 7. Real-Life Example: Normal Browser vs Incognito

When I log in to a website using a normal browser and open a student page, it can open directly because the browser already has my authenticated session.

However, when I open the same URL in an Incognito window, it asks me to log in again because the Incognito window does not have my existing login session.

This demonstrates why authentication is important for protecting private resources.

## Authentication Flow

1. Register User.
2. Store user information and hashed password.
3. Login the User.
4. Validate username and password.
5. Generate JWT Token.
6. Return the token to the client.
7. Send the token with protected API requests.
8. Validate the token before allowing access.

## Conclusion

In this video, I learned the basic concepts of Authentication, Authorization and JWT in FastAPI.

This video was mainly an introduction to the authentication process. The detailed implementation and practical working of JWT authentication will be covered in the upcoming videos.
