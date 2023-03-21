 import unittest
from foryou import get_recommendations

class TestForYou(unittest.TestCase):
    
    def test_get_recommendations(self):
        # Test with a list of posts and a user ID
        posts = [
            {
                "id": 1,
                "title": "Post 1",
                "category": "Software",
                "tags": ["Python", "Programming"]
            },
            {
                "id": 2,
                "title": "Post 2",
                "category": "Technology",
                "tags": ["AI", "Machine Learning"]
            },
            {
                "id": 3,
                "title": "Post 3",
                "category": "Lifestyle",
                "tags": ["Fitness", "Health"]
            },
            {
                "id": 4,
                "title": "Post 4",
                "category": "Software",
                "tags": ["JavaScript", "Web Development"]
            },
            {
                "id": 5,
                "title": "Post 5",
                "category": "Food",
                "tags": ["Recipes", "Cooking"]
            }
        ]
        user_id = 12345
        
        # Test that the function returns a list of recommended posts
        self.assertIsInstance(get_recommendations(posts, user_id), list)
        
        # Test that the recommended posts have the correct format
        for post in get_recommendations(posts, user_id):
            self.assertIsInstance(post, dict)
            self.assertIn("id", post)
            self.assertIn("title", post)
            self.assertIn("category", post)
            self.assertIn("tags", post)
