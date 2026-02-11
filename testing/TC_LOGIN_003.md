# Test case: Login page

# Test case ID: TC-LOGIN-003

# Title:
    check no login with incomplete credentials.

# Module:
    Authentication/login

# Preconditions:
    A valid user's account password
    User must be on a login page

# Test steps:
    1. Navigate to the login page.
    2. leave the username/email field empty 
    3. fill the password field with the correct password of a user account
    4. click the submit button

# Expected Result:
    1. An error should occur indicating that the username/email field must be filled.
    2. The user is kept on the same login page until all valid information is entered.
    3. No user session is made because of incomeplete credentials.

