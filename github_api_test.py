""" The primary goal of this file is to demonstrate a simple unittest implementation

    author: @fizgi
    date: 16-Mar-2021
    python: v3.9.2
"""

import unittest
from unittest import mock
from github_api import get_github_info


class TestGithubAPI(unittest.TestCase):
    """ Test class of the methods """

    @mock.patch('github_api.get_github_info')
    def test_user_id(self, mock_user_id):
        """ test if the request returns a valid response with the given user_id """
        mock_user_id.return_value = False
        info = get_github_info('this_is_not_a_valid_user_id')
        self.assertEqual(mock_user_id.return_value, info)

    @mock.patch('github_api.get_github_info')
    def test_repo_commit_count(self, mock_commit_count):
        mock_commit_count.return_value = 30
        repos = get_github_info('richkempinski')
        commit_count = repos['hellogitworld']
        self.assertEqual(commit_count, 30)

    @mock.patch('github_api.get_github_info')
    def test_repo_repository_count(self, mock_repository_count):
        mock_repository_count.return_value = 9
        repository_count = len(get_github_info('richkempinski'))
        self.assertEqual(repository_count, 9)


if __name__ == '__main__':
    unittest.main()
