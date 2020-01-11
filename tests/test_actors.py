from unittest.mock import patch
from .base import BaseTestCase
from app.routes import actors


class ActorsTestCase(BaseTestCase):

    @patch('app.routes.actors.get_actors')
    def test_get_actors(self, mock_get):
        """Test get actors."""

        mock_get.return_value.status_code = 200
        response = actors.get_actors()
        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)

    @patch('app.routes.actors.add_actor')
    def test_add_actor(self, mock_post):
        """Test add actor."""

        mock_post.return_value.status_code = 201
        response = actors.add_actor()
        self.assertEqual(response.status_code, 201)
