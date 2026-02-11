# Test case: Login page

# Test case ID: TC-LOGIN-002

# Title:
    check errors on login page with incomplete user data

# module:
    Authentication/login

# Preconditions:
    --> A valid username/email must be known
    --> User is on the login page

# Test Steps:
    1. Navigate to the login page of the application
    2. Enter the valid email or username
    3. Leave the password field empty
    4. Click the login button

# Expected Result:
    --> The page should display an error password is required. 
    --> The user is kept on the same login page.
    --> No session is made for the user until is authorised by giving correct credentials
