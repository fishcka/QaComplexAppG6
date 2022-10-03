from pages.utils import Post


class TestCreatePostPage:

    def test_create_post_page(self, login):
        # Navigate to create Post Page
        create_post_page = login.header.navigate_to_create_post_page()
        # Create Post
        post = Post()
        post.fill_default_post()
        create_post_page.create_post(post)
        # Verify the result
        create_post_page.verify_successfully_created()
