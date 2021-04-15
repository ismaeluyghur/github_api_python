import request_util

# you can change 'facebook/react/issues' part of the url to test different repo
url = 'https://api.github.com/repos/facebook/react/issues'
# you can change/add query to test any available filter -- &labels:bug
query = '?q=state:open'
# your github user name
username = '********'
# your github access token
token = '*********'

request_util.get_issue_has_pull_request(url, query,  username, token)