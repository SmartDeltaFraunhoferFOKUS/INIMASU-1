import requests
import json


def download_issues(repo_owner, repo_name, access_token):
    base_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
    issues = []

    page = 1
    while True:
        # Fetch a page of issues from the GitHub API, including the access token
        headers = {'Authorization': f'token {access_token}'}
        response = requests.get(f'{base_url}?state=all&page={page}', headers=headers)

        if response.status_code != 200:
            print(f'Error retrieving issues: {response.text}')
            return

        page_issues = response.json()

        if not page_issues:
            # No more issues found, stop pagination
            break

        issues.extend(page_issues)
        page += 1

    return issues

def get_issues_in_json(repo_owner,repo_name, access_token):
    # Download the issues
    all_issues = download_issues(repo_owner, repo_name, access_token)

    if all_issues:
        # Store the issues in a JSON file
        file_path = f'next.js_{repo_owner}_issues.json'
        with open(file_path, 'w') as file:
            json.dump(all_issues, file, indent=4)

        print(f'All issues have been downloaded and stored in {file_path}.')
    else:
        print('No issues found or an error occurred during the download.')


def get_issues_in_json_file(repo_owner,repo_name, access_token, file_path):
    # Download the issues
    all_issues = download_issues(repo_owner, repo_name, access_token)

    if all_issues:
        # Store the issues in a JSON file
        with open(file_path, 'w') as file:
            json.dump(all_issues, file, indent=4)

        print(f'All issues have been downloaded and stored in {file_path}.')
        return True
    else:
        print('No issues found or an error occurred during the download.')
        return False
