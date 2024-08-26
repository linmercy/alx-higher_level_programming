#!/usr/bin/python3
import requests
import sys

def list_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()
    
    # Check if we received an error response
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    # Print the 10 most recent commits
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
    else:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        list_commits(repo_name, owner_name)

