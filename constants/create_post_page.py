class CreatePostPageConstants:
    TITLE_FIELD_XPATH = ".//input[@id='post-title']"
    BODY_FIELD_XPATH = ".//textarea[@id='post-body']"
    SAVE_NEW_POST_BUTTON_XPATH = ".//button[@class='btn btn-primary']"
    SUCCESS_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    SUCCESS_MESSAGE_TEXT = "New post successfully created."
    CHECK_BOX_XPATH = ".//input[@type='checkbox']"
    SELECT_OPTION_XPATH = ".//select[@id='select1']/option[@value='{option}']"
    OPTION_ALL_USERS = "All Users"
    OPTION_ONE_PERSON = "One Person"
    OPTION_GROUP_MESSAGE = "Group Message"
    TITLE_XPATH = ".//h2[contains(text(),'{title}')]"
    BODY_XPATH = ".//p[contains(text(),'{body}')]"
    UNIQUE_XPATH = ".//p[contains(text(),'Is this post unique? : {unique}')]"
    VISIBILITY_XPATH = ".//u[contains(text(),'{visibility}')]"
