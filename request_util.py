import requests


# pip install requests_mock


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

# mocking function to test the GET api function above
def test_get_updated_issues_multiple_pages(self):
    with open("issues_multiple_first_page.json", "r") as issues_first_file:
        mock_response_first_page = issues_first_file.read()

    with open("issues_multiple_second_page.json", "r") as issues_second_file:
        mock_response_second_page = issues_second_file.read()

    expected_result = [
        {'expand': 'operations,versionedRepresentations,editmeta,changelog,renderedFields', 'id': '10005',
         'self': 'https://jira_url/rest/api/2/issue/10005', 'key': 'MYB-5'},
        {'expand': 'operations,versionedRepresentations,editmeta,changelog,renderedFields', 'id': '10004',
         'self': 'https://jira_url/rest/api/2/issue/10004', 'key': 'MYB-4'},
        {'expand': 'operations,versionedRepresentations,editmeta,changelog,renderedFields', 'id': '10006',
         'self': 'https://jira_url/rest/api/2/issue/10006', 'key': 'MYB-6'}]

    with requests_mock.Mocker() as m:
        m.register_uri('GET', '/rest/api/2/search', [{'text': mock_response_first_page},
                                                     {'text': mock_response_second_page}])
        response = jiratimereport.get_updated_issues("https://jira_url", "user_name", "api_token", "MYB",
                                                     "2020-01-10", "2020-01-20", "")

    self.assertEqual(expected_result, response)
