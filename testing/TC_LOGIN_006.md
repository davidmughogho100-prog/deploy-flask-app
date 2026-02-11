# Test Case: Login Page 

# Title:
    check if the application allows uploading of large ammounts of data in the input fields

# Module:
    Authentication/login

# preconditions
    The user must be on the login page of the application

# Test steps
    1. Open a very big document 
    2. press ctrl + A to copy all its content
    3. navigate to the login url of the website
    5. In the email/username field press ctrl + V to paste all its contents into the field.
    6. In the password field press ctrl + v to paste all contents into the field as well.
    7. click the login button

# Expected Result:
    The app must not process the uploaded data to preserve memory or query it against the database
    The app must not display invalid username or password


