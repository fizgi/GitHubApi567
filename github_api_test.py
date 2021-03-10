""" The primary goal of this file is to demonstrate a simple unittest implementation

    author: @fizgi
    date: 09-Mar-2021
    python: v3.9.2
"""

import unittest
from github_api import get_github_info


class TestGithubAPI(unittest.TestCase):
    """ Test class of the methods """

    def test_user_id(self):
        """ test if the request returns a valid response with the given user_id """
        self.assertFalse(get_github_info('this_is_not_a_valid_user_id'))
        self.assertFalse(get_github_info('another_non_valid_user_id'))

    def test_repo_commit_count(self):
        repos = get_github_info('richkempinski')

        self.assertEqual(repos['try_nbdev'], 2)
        self.assertEqual(repos['try_nbdev2'], 5)
        self.assertEqual(repos['Mocks'], 10)
        self.assertEqual(repos['hellogitworld'], 30)

    def test_repo_repository_count(self):
        richk_repo_count = len(get_github_info('richkempinski'))
        self.assertEqual(richk_repo_count, 9)

        fizgi_repo_count = len(get_github_info('fizgi'))
        self.assertEqual(fizgi_repo_count, 29)

        raz_repo_count = len(get_github_info('raziehsaremi'))
        self.assertEqual(raz_repo_count, 6)


if __name__ == '__main__':
    unittest.main()
