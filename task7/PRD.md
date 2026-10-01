# Student Registration Portal — Product Requirements Document

**Version:** 1.0  
**Status:** Initial working version

## 1. Purpose

The Student Registration Portal lets an account holder sign up, log in, enter student registration details, and review the student records they have submitted.

## 2. Goals

- Provide a clear home page with sign-up and login links.
- Let new users create an account and existing users log in.
- Protect the student registration page so only logged-in users can access it.
- Save student records and show each account holder their own records.
- Give clear feedback for invalid, duplicate, and successful submissions.

## 3. Users

- **Visitor:** can view the home page, create an account, or log in.
- **Account holder:** can access the student registration form and view records associated with their account.

## 4. User flow

1. A visitor opens the home page.
2. The visitor signs up or logs in.
3. After successful login, the account holder reaches the student registration page.
4. The account holder submits a student ID, name, semester, and subject.
5. The portal saves the record and displays it in the registered students list.

## 5. Functional requirements

### Account creation

- The sign-up form collects username, name, and password.
- All fields are required. Usernames must be unique.
- Passwords are stored as hashes.
- Missing fields and duplicate usernames produce an error message.
- Successful sign-up sends the user to the login page.

### Login and access

- The login form collects username and password.
- Valid credentials create a session and send the user to student registration.
- Invalid credentials display an error message.
- Unauthenticated visitors who open the student registration page are sent to login.

### Student registration

- The form collects student ID, student name, semester, and subject.
- All fields are required, and student IDs must be unique.
- Each record is associated with the account that submitted it.
- A successful submission is saved and shown in the registered students list.
- The list contains only records associated with the current account and is sorted by student name.
- Missing fields and duplicate student IDs produce an error message.

### Pages and styling

- The portal provides Home, Sign up, Login, and Student Registration pages.
- All pages use the shared stylesheet at `myuser/static/myuser/css/style.css`.
- The layout supports desktop and narrow mobile screens.

## 6. Data

### Account

- Username: required, unique, maximum 20 characters.
- Name: required, maximum 50 characters.
- Password: required, stored as a hash.

### Student registration

- Student ID: required, unique, maximum 20 characters.
- Student name: required, maximum 100 characters.
- Semester: required, maximum 30 characters.
- Subject: required, maximum 100 characters.
- Registered by: account that submitted the record.

## 7. Security and privacy

- Passwords must remain hashed in storage.
- Form submissions use Django CSRF protection.
- Student records are filtered by the current account.
- Login state is maintained through a Django session.

## 8. Out of scope for this version

- Logout controls, password reset, and email verification.
- Editing or deleting account and student records.
- Search, pagination, and administrator reporting screens.

## 9. Acceptance criteria

- A visitor can create an account with a unique username and then log in.
- Duplicate usernames and invalid login attempts show useful errors.
- A logged-in account holder can submit a complete student registration.
- A duplicate student ID is rejected with a useful error.
- Successful submissions appear in that account holder's list.
- A different account cannot view another account's student records.
- The pages load with the shared CSS and remain usable on mobile-sized screens.
