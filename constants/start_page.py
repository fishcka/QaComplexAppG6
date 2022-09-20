class StartPageConstants:
    # Sign In
    SIGN_IN_USERNAME_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_ERROR_MESSAGE_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_ERROR_MESSAGE_TEXT = "Invalid username / pasword"
    SIGN_IN_BUTTON_XPATH = ".//button[text()='Sign In']"

    # Sign Up
    SIGN_UP_USERNAME_FIELD_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_FIELD_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"

    # TODO: next page
    MY_PROFILE_BUTTON_XPATH = ".//img[@alt='My profile']"
    SIGN_OUT_BUTTON_XPATH = ".//button[text()='Sign Out']"  # .//button[@class='btn btn-sm btn-secondary']
