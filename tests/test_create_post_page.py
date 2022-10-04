from constants.create_post_page import CreatePostPageConstants
from pages.utils import Post


class TestCreatePostPage:

    def test_create_post_page(self, login, page_driver):
        # Navigate to create Post Page
        create_post_page = login.header.navigate_to_create_post_page()
        # Create Post
        post = Post(unique="yes", visibility=CreatePostPageConstants.OPTION_ONE_PERSON)
        post.fill_default_post()
        create_post_page.create_post(post, page_driver)
        # Verify the result
        create_post_page.verify_successfully_created()
        create_post_page.verify_all_attributes(post)
