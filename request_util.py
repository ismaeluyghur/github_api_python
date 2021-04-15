import requests


def get_issue_has_pull_request(url, query, username, token):
    total_issues = []
    issues_with_pull_request = []

    response = requests.get(url + query, auth=(username, token))
    data = response.json()
    total_issues = total_issues + data

    while 'next' in response.links:
        print("Next page found, downloading", response.links['next']['url'])
        response = requests.get(response.links['next']['url'], auth=(username, token))
        data = response.json()
        total_issues = total_issues + data

    for i in total_issues:
        if 'pull_request' in i:
            issues_with_pull_request.append(i)

    print(len(issues_with_pull_request))
