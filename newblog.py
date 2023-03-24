import unittest
from selenium import webdriver

class TestNewBlogPost(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://teen-s-blogs.github.io/Grey-Blogs/blogs.html")

    def test_create_new_post(self):
        # Fill in the form fields
        user_id_input = self.driver.find_element_by_id("user_id")
        user_id_input.send_keys("my_user_id")
        title_input = self.driver.find_element_by_id("title")
        title_input.send_keys("My New Blog Post")
        tag_input = self.driver.find_element_by_id("tag")
        tag_input.send_keys("my, tags")
        content_input = self.driver.find_element_by_id("content")
        content_input.send_keys("This is the content of my new blog post.")

        # Submit the form
        submit_button = self.driver.find_element_by_xpath("//input[@type='submit']")
        submit_button.click()

        # Check if the new post was created
        posts_link = self.driver.find_element_by_xpath("//li/a[text()='My Posts']")
        posts_link.click()
        new_post_title = self.driver.find_element_by_xpath("//h3[text()='My New Blog Post']")
        self.assertEqual(new_post_title.text, "My New Blog Post")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
