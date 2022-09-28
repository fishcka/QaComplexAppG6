from pages.utils import random_symbols


class TestCreatePostPage:

    def test_create_post_page(self, login):
        # Navigate to create Post Page
        header = login.navigate_to_create_post_page()
        # Create Post
        header.create_post(title=random_symbols(15), body=random_symbols(150))
        # Verify the result
        header.verify_successfully_created()
