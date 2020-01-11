from unittest.mock import patch
from .base import BaseTestCase
from app.routes import movies


class MoviesTestCase(BaseTestCase):

    @patch('app.routes.movies.get_movies')
    def test_get_movies(self, mock_get):
        """Test get movies."""

        mock_get.return_value.status_code = 200
        response = movies.get_movies()
        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)

    @patch('app.routes.movies.add_movie')
    def test_add_movie(self, mock_post):
        """Test add movie."""

        mock_post.return_value.status_code = 201
        response = movies.add_movie()
        self.assertEqual(response.status_code, 201)
