# Node.js + Express Todo API — Authentication, Authorization & JSON Database

## Maximum Marks — 30

### Assignment Objective

Build a production-style **Todo REST API** using **Node.js and Express**.

The application must support multiple users. Each user must be able to register, log in, manage authentication tokens, and perform CRUD operations only on their own todos.

For this assignment, **`db.json` will be used as the database**. You must not use MongoDB, PostgreSQL, MySQL, SQLite, Firebase, or any other external database.

The purpose of this assignment is to evaluate your understanding of:

* Express.js
* REST API design
* JSON-file persistence
* Authentication
* Authorization
* Password hashing
* Access tokens
* Refresh tokens
* Token expiration
* Logout
* Middleware
* Input validation
* HTTP status codes
* Error handling
* File-system operations
* Edge cases
* API security

---

# 1. Environment Requirements

* Use Node.js LTS.
* The expected Node.js version is:

```text
v16.16.0
```

* Do not change or override the existing `package.json`.
* Do not push `package-lock.json`.

Install dependencies using:

```bash
npm install --engine-strict
```

Run the tests using:

```bash
npm run test
```

### Important

Before running the test suite:

* Make sure your Express server is **not already running locally**.
* Make sure `db.json` exists in the expected location.
* Do not modify the test files.
* Do not hard-code responses only to satisfy the test cases.

---

# 2. Application Requirements

Create a Todo API server using Express.

The main application must be created in:

```text
index.js
```

and the Express application must be exported.

Example:

```js
module.exports = app;
```

The application must return JSON responses.

---

# 3. Database

Use:

```text
db.json
```

as the application's database.

The initial database structure must be:

```json
{
  "users": [],
  "todos": [],
  "refreshTokens": []
}
```

You may add additional fields if required, but the existing top-level structure must remain compatible.

For example:

```json
{
  "users": [],
  "todos": [],
  "refreshTokens": []
}
```

### Example User

```json
{
  "id": 1,
  "name": "John",
  "email": "john@example.com",
  "password": "$2b$10$hashedPassword",
  "createdAt": "2026-08-21T10:00:00.000Z"
}
```

### Example Todo

```json
{
  "id": 1,
  "userId": 1,
  "task": "Learn Node.js",
  "status": false,
  "createdAt": "2026-08-21T10:30:00.000Z",
  "updatedAt": "2026-08-21T10:30:00.000Z"
}
```

### Important Security Rule

**Never store a user's plain-text password in `db.json`.**

Incorrect:

```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

Correct:

```json
{
  "email": "john@example.com",
  "password": "$2b$10$..."
}
```

Passwords must be hashed using a suitable password-hashing library such as bcrypt.

---

# 4. Authentication vs Authorization

You must understand the difference between these two concepts.

## Authentication

Authentication answers:

> "Who are you?"

For example:

```text
User sends email + password
        ↓
Server verifies credentials
        ↓
Server issues access token
        ↓
User is authenticated
```

## Authorization

Authorization answers:

> "Are you allowed to perform this operation?"

For example:

User A owns:

```text
Todo 1
Todo 2
```

User B owns:

```text
Todo 3
```

User A must **not** be able to update or delete Todo 3.

The server must check ownership.

---

# 5. Required API Routes

Your API must implement the following routes.

## Authentication Routes

```text
POST /auth/register
POST /auth/login
POST /auth/refresh
POST /auth/logout
```

## Todo Routes

```text
GET    /todos
POST   /todos
GET    /todos/:id
PUT    /todos/:id
DELETE /todos/:id
```

All Todo routes must require authentication.

---

# 6. POST /auth/register

Creates a new user.

### Request

```http
POST /auth/register
Content-Type: application/json
```

```json
{
  "name": "John",
  "email": "john@example.com",
  "password": "password123"
}
```

### Validation Requirements

The server must validate:

* `name` is present.
* `email` is present.
* Email must have a valid format.
* Password is present.
* Password must have a reasonable minimum length.
* Email must be unique.

### Successful Response

Status:

```text
201 Created
```

Example:

```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "name": "John",
    "email": "john@example.com"
  }
}
```

### Important

Do **not** return:

```json
{
  "password": "password123"
}
```

The password must never appear in the API response.

---

# 7. Registration Scenarios

### Scenario 1 — Successful registration

Request:

```json
{
  "name": "John",
  "email": "john@example.com",
  "password": "password123"
}
```

Expected:

```text
201 Created
```

---

### Scenario 2 — Duplicate email

A user already exists:

```json
{
  "email": "john@example.com"
}
```

Another registration attempt:

```json
{
  "name": "Another John",
  "email": "john@example.com",
  "password": "password123"
}
```

Expected:

```text
409 Conflict
```

Example:

```json
{
  "message": "Email already registered"
}
```

---

### Scenario 3 — Missing password

```json
{
  "name": "John",
  "email": "john@example.com"
}
```

Expected:

```text
400 Bad Request
```

---

### Scenario 4 — Invalid email

```json
{
  "name": "John",
  "email": "hello",
  "password": "password123"
}
```

Expected:

```text
400 Bad Request
```

---

# 8. POST /auth/login

Authenticates an existing user.

### Request

```http
POST /auth/login
Content-Type: application/json
```

```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

The server must:

1. Find the user.
2. Compare the supplied password with the stored password hash.
3. Reject invalid credentials.
4. Generate an access token.
5. Generate a refresh token.
6. Store the refresh-token information in `db.json`.

### Successful Response

Status:

```text
200 OK
```

Example:

```json
{
  "message": "Login successful",
  "accessToken": "ACCESS_TOKEN_HERE",
  "refreshToken": "REFRESH_TOKEN_HERE"
}
```

---

# 9. Invalid Login Scenarios

### Wrong password

```json
{
  "email": "john@example.com",
  "password": "wrong-password"
}
```

Expected:

```text
401 Unauthorized
```

---

### Non-existent user

```json
{
  "email": "doesnotexist@example.com",
  "password": "password123"
}
```

Expected:

```text
401 Unauthorized
```

Do not reveal unnecessary information such as:

```text
User does not exist
```

A generic authentication error is preferable.

Example:

```json
{
  "message": "Invalid credentials"
}
```

---

# 10. Access Token

After successful login, the client receives an access token.

The client must send the access token using:

```http
Authorization: Bearer <access-token>
```

Example:

```http
Authorization: Bearer eyJhbGciOi...
```

The Todo API must reject requests that do not contain a valid access token.

---

# 11. Authentication Middleware

Create authentication middleware.

For example:

```text
middleware/auth.js
```

The middleware should:

1. Read the `Authorization` header.
2. Verify that it uses the Bearer format.
3. Extract the token.
4. Verify the token.
5. Identify the user.
6. Attach the authenticated user information to the request.

Conceptually:

```text
Request
   ↓
Authorization header
   ↓
Extract Bearer token
   ↓
Verify token
   ↓
Find authenticated user
   ↓
req.user
   ↓
Controller
```

For example:

```js
req.user = {
  id: 1,
  email: "john@example.com"
};
```

Do not trust a `userId` supplied by the client when the authenticated user's identity is already available from the token.

---

# 12. Authentication Error Cases

The API must correctly handle:

### No Authorization header

```http
GET /todos
```

Expected:

```text
401 Unauthorized
```

---

### Invalid format

```http
Authorization: abcdef
```

Expected:

```text
401 Unauthorized
```

---

### Invalid token

```http
Authorization: Bearer invalid-token
```

Expected:

```text
401 Unauthorized
```

---

### Expired token

Expected:

```text
401 Unauthorized
```

The response should indicate that authentication is required or that the token is expired.

---

# 13. Refresh Tokens

Implement refresh-token functionality.

Access tokens should have a relatively short lifetime.

Refresh tokens should have a longer lifetime.

Example concept:

```text
Access Token
    ↓
Short-lived
    ↓
Used for API requests

Refresh Token
    ↓
Longer-lived
    ↓
Used to obtain a new access token
```

The exact expiration durations may be decided by the implementation, but they must be configurable rather than scattered as magic values throughout the application.

---

# 14. POST /auth/refresh

Used to generate a new access token.

### Request

```json
{
  "refreshToken": "REFRESH_TOKEN_HERE"
}
```

The server must verify:

* The refresh token exists.
* The refresh token has not expired.
* The refresh token has not been revoked.
* The token belongs to a valid user.

### Successful Response

```text
200 OK
```

Example:

```json
{
  "accessToken": "NEW_ACCESS_TOKEN"
}
```

---

# 15. Refresh Token Scenarios

### Valid refresh token

Expected:

```text
200 OK
```

A new access token is returned.

---

### Invalid refresh token

```json
{
  "refreshToken": "invalid-token"
}
```

Expected:

```text
401 Unauthorized
```

---

### Expired refresh token

Expected:

```text
401 Unauthorized
```

---

### Revoked refresh token

Expected:

```text
401 Unauthorized
```

---

# 16. POST /auth/logout

Logout must invalidate the refresh token.

### Request

```json
{
  "refreshToken": "REFRESH_TOKEN_HERE"
}
```

The server should mark the token as revoked or remove it from the active refresh-token store.

Example:

```json
{
  "id": "token-id",
  "userId": 1,
  "token": "hashed-or-secure-token",
  "expiresAt": "2026-09-21T10:00:00.000Z",
  "revoked": true
}
```

After logout, attempting to use that refresh token must fail.

Expected:

```text
200 OK
```

---

# 17. Todo Ownership

Every Todo must belong to a user.

Example:

```json
{
  "id": 1,
  "userId": 10,
  "task": "Learn Express",
  "status": false
}
```

The `userId` should come from the authenticated user.

Do **not** rely on:

```json
{
  "userId": 10
}
```

provided by the client.

For example, if the token identifies the user as:

```text
userId = 10
```

then the server should internally create:

```json
{
  "userId": 10
}
```

---

# 18. GET /todos

Returns the todos belonging to the authenticated user.

### Request

```http
GET /todos
Authorization: Bearer <access-token>
```

### Response

```text
200 OK
```

Example:

```json
{
  "todos": [
    {
      "id": 1,
      "userId": 1,
      "task": "Learn Node.js",
      "status": false
    },
    {
      "id": 2,
      "userId": 1,
      "task": "Learn Express",
      "status": true
    }
  ]
}
```

User A must not receive User B's todos.

---

# 19. POST /todos

Creates a Todo for the authenticated user.

### Request

```http
POST /todos
Authorization: Bearer <access-token>
Content-Type: application/json
```

```json
{
  "task": "Learn Node.js",
  "status": false
}
```

### Response

```text
201 Created
```

Example:

```json
{
  "todo": {
    "id": 1,
    "userId": 1,
    "task": "Learn Node.js",
    "status": false
  }
}
```

The server must generate the Todo ID.

The client should **not** be trusted to generate IDs.

---

# 20. POST Todo Validation

The following should be rejected:

### Missing task

```json
{
  "status": false
}
```

Expected:

```text
400 Bad Request
```

---

### Empty task

```json
{
  "task": "",
  "status": false
}
```

Expected:

```text
400 Bad Request
```

---

### Invalid status

```json
{
  "task": "Learn Node",
  "status": "hello"
}
```

Expected:

```text
400 Bad Request
```

`status` should be a boolean.

Valid:

```json
true
```

or:

```json
false
```

---

# 21. GET /todos/:id

Returns a single Todo belonging to the authenticated user.

Example:

```http
GET /todos/10
Authorization: Bearer <access-token>
```

If Todo 10 belongs to the authenticated user:

```text
200 OK
```

If the Todo does not exist:

```text
404 Not Found
```

If the Todo exists but belongs to another user:

```text
403 Forbidden
```

The implementation may choose to return `404` for cross-user resources as an additional security measure, provided the behavior is consistent.

---

# 22. PUT /todos/:id

Updates a Todo.

Example:

```http
PUT /todos/1
Authorization: Bearer <access-token>
Content-Type: application/json
```

```json
{
  "task": "Learn advanced Node.js",
  "status": true
}
```

### Successful Response

```text
200 OK
```

Example:

```json
{
  "todo": {
    "id": 1,
    "userId": 1,
    "task": "Learn advanced Node.js",
    "status": true
  }
}
```

---

# 23. PUT Error Conditions

The API must handle all of the following.

### Invalid ID

```http
PUT /todos/abc
```

Expected:

```text
400 Bad Request
```

---

### Todo does not exist

```http
PUT /todos/99999
```

Expected:

```text
404 Not Found
```

---

### Todo belongs to another user

Expected:

```text
403 Forbidden
```

or a deliberate security-oriented `404 Not Found`.

---

### Invalid body

```json
{
  "status": "completed"
}
```

Expected:

```text
400 Bad Request
```

---

### Missing body

```http
PUT /todos/1
```

Expected:

```text
400 Bad Request
```

---

# 24. DELETE /todos/:id

Deletes a Todo belonging to the authenticated user.

Example:

```http
DELETE /todos/1
Authorization: Bearer <access-token>
```

### Successful Response

```text
200 OK
```

Example:

```json
{
  "message": "Todo deleted successfully"
}
```

---

# 25. DELETE Error Conditions

### Invalid ID

```http
DELETE /todos/abc
```

Expected:

```text
400 Bad Request
```

---

### Todo does not exist

```http
DELETE /todos/99999
```

Expected:

```text
404 Not Found
```

---

### Todo belongs to another user

Expected:

```text
403 Forbidden
```

or a deliberate security-oriented `404 Not Found`.

---

# 26. Authorization Scenario

This is an important part of the assignment.

Suppose we have:

### User A

```text
id: 1
email: alice@example.com
```

Alice creates:

```json
{
  "id": 1,
  "userId": 1,
  "task": "Alice's todo"
}
```

### User B

```text
id: 2
email: bob@example.com
```

Bob attempts:

```http
DELETE /todos/1
Authorization: Bearer <Bob's token>
```

The server must **not** delete Alice's Todo.

This is an authorization failure.

---

# 27. Authentication vs Authorization Example

### Authentication failure

Bob sends:

```http
GET /todos
```

without a token.

The server says:

```text
401 Unauthorized
```

Meaning:

> "I don't know who you are."

### Authorization failure

Bob sends a valid token but attempts to modify Alice's Todo.

The server says:

```text
403 Forbidden
```

Meaning:

> "I know who you are, but you are not allowed to do this."

Understanding this difference is an important learning objective.

---

# 28. ID Generation

IDs must be numeric.

Do not depend on the client to provide a unique ID.

For example, if:

```json
{
  "todos": [
    { "id": 1 },
    { "id": 2 },
    { "id": 5 }
  ]
}
```

the next ID should not accidentally overwrite an existing Todo.

You must implement a reliable ID-generation strategy.

The same principle applies to user IDs.

---

# 29. JSON Database File Handling

The application must handle file-system problems gracefully.

The application should be able to recover when:

* `db.json` does not exist.
* The directory containing `db.json` does not exist.
* `db.json` is empty.
* `db.json` contains invalid JSON.
* Required arrays are missing.

For example, if the database file does not exist, the application should be able to create the required structure:

```json
{
  "users": [],
  "todos": [],
  "refreshTokens": []
}
```

---

# 30. Invalid Database Example

Suppose `db.json` contains:

```text
this is not json
```

The application must not silently behave as though the database contains no users.

Handle the error appropriately.

The application should either:

* safely initialize a valid database where appropriate, or
* return/log a clear server-side error.

Do not expose internal file-system details to API clients.

---

# 31. Concurrency Consideration

Because `db.json` is being used instead of a real database, multiple writes can cause problems.

For example:

```text
Request A → read db.json
Request B → read db.json
Request A → write db.json
Request B → write db.json
```

Request B could accidentally overwrite changes from Request A.

The implementation should therefore keep file reads/writes predictable and avoid unnecessary simultaneous writes.

You are not expected to build a full database engine, but you should understand that JSON files do not provide the same guarantees as real databases.

---

# 32. Response Format

All API responses must be JSON.

Do not return:

```text
Todo deleted
```

Return:

```json
{
  "message": "Todo deleted successfully"
}
```

Error responses should also be JSON.

Example:

```json
{
  "message": "Invalid todo ID"
}
```

Do not return HTML error pages.

---

# 33. HTTP Status Codes

Use status codes appropriately.

| Situation                      | Status |
| ------------------------------ | -----: |
| Successful GET                 |    200 |
| Successful PUT                 |    200 |
| Successful DELETE              |    200 |
| Successful login               |    200 |
| Successful refresh             |    200 |
| Successful logout              |    200 |
| Successful registration        |    201 |
| Successful Todo creation       |    201 |
| Invalid request                |    400 |
| Missing/invalid authentication |    401 |
| Authenticated but not allowed  |    403 |
| Resource does not exist        |    404 |
| Duplicate registration         |    409 |
| Unexpected server error        |    500 |

Do not return `200` for every possible situation.

---

# 34. Error Handling

Create centralized error handling where appropriate.

The server must not crash because of:

* Invalid JSON request bodies.
* Invalid Todo IDs.
* Missing fields.
* Invalid authentication headers.
* Invalid tokens.
* Missing files.
* Invalid database contents.
* Non-existent resources.

Internal errors should be logged appropriately but should not expose sensitive implementation details to the client.

Avoid responses such as:

```json
{
  "error": "ENOENT: no such file or directory, open '/home/user/project/db.json'"
}
```

Instead return something appropriate such as:

```json
{
  "message": "Internal server error"
}
```

---

# 35. Security Requirements

The application must follow these rules.

### Passwords

* Never store plain-text passwords.
* Never return passwords in API responses.
* Never log passwords.

### Tokens

* Access tokens must expire.
* Refresh tokens must expire.
* Refresh tokens must be revocable.
* Logout must invalidate the refresh token.
* Do not place sensitive information unnecessarily inside tokens.

### Authorization

* Never trust `userId` from the request body.
* Always determine the user from the authenticated token.
* Verify ownership before modifying or deleting a Todo.

### Input

Never blindly trust:

```text
req.body
req.params
req.headers
```

Validate them before using them.

---

# 36. Suggested Project Structure

You are free to organize the project differently, but the following structure is recommended:

```text
project/
│
├── index.js
├── db.json
├── package.json
│
├── routes/
│   ├── auth.js
│   └── todos.js
│
├── controllers/
│   ├── authController.js
│   └── todoController.js
│
├── middleware/
│   ├── auth.js
│   ├── errorHandler.js
│   └── validation.js
│
├── services/
│   ├── database.js
│   └── tokenService.js
│
└── utils/
    └── validation.js
```

This structure is a recommendation, not a strict requirement.

---

# 37. Complete User Journey Example

The following is the expected application flow.

## Step 1 — Register

```http
POST /auth/register
```

```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "password": "password123"
}
```

Server creates the user.

---

## Step 2 — Login

```http
POST /auth/login
```

```json
{
  "email": "alice@example.com",
  "password": "password123"
}
```

Server returns:

```json
{
  "accessToken": "...",
  "refreshToken": "..."
}
```

---

## Step 3 — Get Todos

```http
GET /todos
Authorization: Bearer <accessToken>
```

Response:

```json
{
  "todos": []
}
```

---

## Step 4 — Create Todo

```http
POST /todos
Authorization: Bearer <accessToken>
```

```json
{
  "task": "Learn Express",
  "status": false
}
```

---

## Step 5 — Update Todo

```http
PUT /todos/1
Authorization: Bearer <accessToken>
```

```json
{
  "task": "Learn Express deeply",
  "status": true
}
```

---

## Step 6 — Delete Todo

```http
DELETE /todos/1
Authorization: Bearer <accessToken>
```

---

## Step 7 — Logout

```http
POST /auth/logout
```

```json
{
  "refreshToken": "..."
}
```

The refresh token must no longer be usable.

---

# 38. Important Test Scenarios

Your implementation should be tested against scenarios such as:

## Authentication

* Register a new user.
* Register duplicate email.
* Register with missing email.
* Register with invalid email.
* Register with missing password.
* Login with correct credentials.
* Login with incorrect password.
* Login with unknown email.
* Access protected route without token.
* Access protected route with invalid token.
* Access protected route with expired token.

## Refresh Tokens

* Refresh using valid token.
* Refresh using invalid token.
* Refresh using expired token.
* Refresh using revoked token.
* Logout successfully.
* Attempt refresh after logout.

## Todos

* Get todos for authenticated user.
* Create Todo.
* Get individual Todo.
* Update Todo.
* Delete Todo.
* Update non-existent Todo.
* Delete non-existent Todo.
* Update using invalid ID.
* Delete using invalid ID.
* Create Todo with missing task.
* Create Todo with invalid status.

## Authorization

* User A can update their own Todo.
* User A can delete their own Todo.
* User A cannot update User B's Todo.
* User A cannot delete User B's Todo.
* User A cannot see User B's todos.

## Database

* Missing `db.json`.
* Missing database directory.
* Empty `db.json`.
* Invalid JSON.
* Missing `users` array.
* Missing `todos` array.
* Missing `refreshTokens` array.

---

# 39. Example End-to-End Scenario

Assume Alice and Bob are registered.

### Alice

```text
User ID: 1
```

### Bob

```text
User ID: 2
```

Alice creates:

```json
{
  "id": 1,
  "userId": 1,
  "task": "Prepare assignment",
  "status": false
}
```

Bob creates:

```json
{
  "id": 2,
  "userId": 2,
  "task": "Learn Express",
  "status": false
}
```

### Alice calls GET /todos

Expected:

```json
{
  "todos": [
    {
      "id": 1,
      "userId": 1,
      "task": "Prepare assignment",
      "status": false
    }
  ]
}
```

Bob's Todo must not appear.

### Bob attempts:

```http
PUT /todos/1
```

with Bob's access token.

The server must reject the request.

This is an **authorization** test.

---

# 40. What the Intern Should Learn

By completing this assignment, the intern should be able to explain:

### Beginner

* What is Express?
* What is a REST API?
* What are GET, POST, PUT and DELETE?
* What is middleware?
* How does `req.body` work?
* How does `req.params` work?
* How does JSON-file persistence work?

### Intermediate

* Why passwords must be hashed.
* What authentication means.
* What authorization means.
* How Bearer tokens work.
* Why access tokens expire.
* Why refresh tokens exist.
* Why logout requires token revocation.
* Why users should only access their own resources.

### Advanced

* How middleware protects routes.
* How token expiration works.
* How refresh-token rotation/revocation can improve security.
* Why file-based databases have concurrency limitations.
* Why input validation is important.
* Why `401` and `403` are different.
* Why internal server errors should not expose implementation details.

---

# 41. Evaluation Criteria

| Requirement                             |  Marks |
| --------------------------------------- | -----: |
| Application starts and can be submitted |      1 |
| Correct Express/API structure           |      1 |
| JSON database implementation            |      2 |
| User registration + validation          |      3 |
| Password hashing                        |      2 |
| Login + access-token authentication     |      3 |
| Refresh-token management                |      3 |
| Logout/token revocation                 |      2 |
| Authentication middleware               |      2 |
| GET todos with user isolation           |      2 |
| POST todo                               |      2 |
| PUT todo + validation/error handling    |      2 |
| DELETE todo + validation/error handling |      2 |
| Authorization/ownership checks          |      2 |
| File/directory error handling           |      1 |
| Code quality and organization           |      1 |
| **Total**                               | **31** |

The evaluator may award partial marks based on implementation quality.

---

# 42. Minimum Acceptance Criteria

A submission should not be considered complete unless:

* The server starts successfully.
* `db.json` is used as the database.
* Users can register.
* Passwords are hashed.
* Users can log in.
* Login returns an access token.
* Protected routes reject unauthenticated requests.
* Users can only access their own Todos.
* Users can create Todos.
* Users can update Todos.
* Users can delete Todos.
* Refresh tokens work.
* Logout invalidates refresh tokens.
* Invalid requests return appropriate HTTP status codes.
* The application does not crash on common invalid inputs.
* Missing database files/directories are handled.
* API responses are JSON.

---

# 43. Final Submission Checklist

Before submitting, verify all of the following:

* [ ] Node.js version is `v16.16.0`.
* [ ] `npm install --engine-strict` works.
* [ ] `package.json` has not been unnecessarily modified.
* [ ] `package-lock.json` is not committed.
* [ ] `index.js` exports the Express application.
* [ ] `db.json` is used as the database.
* [ ] Database starts with `users`, `todos`, and `refreshTokens`.
* [ ] Registration works.
* [ ] Duplicate registration is rejected.
* [ ] Passwords are hashed.
* [ ] Passwords are never returned in responses.
* [ ] Login works.
* [ ] Access tokens expire.
* [ ] Protected routes require authentication.
* [ ] Refresh tokens work.
* [ ] Refresh tokens expire.
* [ ] Logout revokes refresh tokens.
* [ ] Users cannot access another user's Todos.
* [ ] GET Todo works.
* [ ] POST Todo works.
* [ ] PUT Todo works.
* [ ] DELETE Todo works.
* [ ] Invalid IDs are handled.
* [ ] Missing resources are handled.
* [ ] Invalid request bodies are handled.
* [ ] Missing `db.json` is handled.
* [ ] Missing database directories are handled.
* [ ] Invalid database JSON is handled.
* [ ] API responses are JSON.
* [ ] Appropriate HTTP status codes are used.
* [ ] `npm run test` passes.
* [ ] Server is stopped before running the local test suite.

---

# 44. General Guidelines

The system used for evaluation may take between **1–20 minutes** to respond.

Read the problem carefully before submitting.

Do not wait until the last minute to submit.

Before submission:

1. Run the application locally.
2. Test registration.
3. Test login.
4. Copy the access token.
5. Test protected Todo routes.
6. Test another user's authorization.
7. Test token refresh.
8. Test logout.
9. Test invalid inputs.
10. Test missing database files.
11. Run the complete test suite.
12. Stop the local server.
13. Submit only after verifying the complete flow.

The goal is not simply to make the happy-path tests pass.

The goal is to build a Todo API that behaves correctly when **valid users, invalid users, expired tokens, unauthorized users, invalid data, missing resources, and file-system failures** are encountered.

---

# 45. Challenge Scenarios

These scenarios are intended for interns who finish the basic requirements early.

### Challenge 1 — Refresh Token Rotation

Instead of allowing the same refresh token to be reused indefinitely, implement refresh-token rotation:

```text
Old refresh token
       ↓
/auth/refresh
       ↓
Old token revoked
       ↓
New refresh token issued
```

If the old token is reused, reject it.

---

### Challenge 2 — Rate Limiting

Protect the login endpoint from excessive requests.

For example:

```text
POST /auth/login
```

should not be allowed to receive unlimited requests from the same client.

---

### Challenge 3 — Pagination

Add:

```text
GET /todos?page=1&limit=10
```

and return only the requested number of Todos.

---

### Challenge 4 — Filtering

Support:

```text
GET /todos?status=true
```

to return only completed Todos.

---

### Challenge 5 — Search

Support:

```text
GET /todos?search=node
```

to search Todo tasks.

---

# Expected Learning Outcome

At the end of this assignment, the intern should be able to build and explain a small **multi-user REST API with authentication and authorization**, rather than only implementing basic CRUD.

They should be able to answer:

> **"How does a request travel from the client, through authentication and authorization middleware, to the Todo controller, and finally get persisted safely into the JSON database?"**

If they can explain and implement that complete flow, the assignment has achieved its purpose.
