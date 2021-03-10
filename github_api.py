""" The primary goal of this file is to get github data of a user

    author: @fizgi
    date: 09-Mar-2021
    python: v3.9.2
"""

import requests
import json


def get_github_info(user):
    response = requests.get(f'https://api.github.com/users/{user}/repos')

    if response.status_code != 200:
        return False

    repos = json.loads(response.text)
    repos_dict = dict()

    for repo in repos:
        name = repo['name']
        response = requests.get(f'https://api.github.com/repos/{user}/{name}/commits')
        commits = json.loads(response.text)
        repos_dict[name] = len(commits)

        print(f"Repo: {name}, Number of commits: {len(commits)}")

    return repos_dict
