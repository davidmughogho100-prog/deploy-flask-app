# Test case: Login Page

# Test case ID: TC-LOGIN-004

# Title:
    check no login with incomplete user account information

# module:
    Authentication/login

# Preconditions:
    The user must be on the login page of the appplication

# Test Steps:
    1. Navigate to the login page
    2. Leave the email/username field empty
    3. leave the password field empty
    4. click the login button

# Expected Result:
    --> User should not be allowed to login due to empty credentials fields.
    --> Error should occur indicating that username/email field is required.
    --> Error should occur indicating that the password field is required.
    --> The user should be kept on the login page until gives valid credentials
    --> no user session is created because of empty input fields

