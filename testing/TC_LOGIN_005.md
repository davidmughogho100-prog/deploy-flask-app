# Test Case: Login Page

# Test case ID: TC-LOGIN-005

# Title:
    verify that too much data can not be uploaded in the input fields

# Module:
    Authentication/Login

# precondition
    User must be on the login page

# Test Steps:
    1. Open a very big document like a pdf
    2. press ctrl + A 
    3. press ctrl + c to copy all its contents
    4. go to the application login url
    5. In the email/password field press ctrl + v to paste all contents of the pdf file
    6. In the password field press ctrl + v to past all contents from the clipboard into it as well


# Expected Result:
    Scrolling left inside the email/username field should have only the first few words of the pasted document.
    Scrolling left inside the password field should have only two or three words from the document
