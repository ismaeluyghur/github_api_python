import request_util

# you can change 'facebook/react/issues' part of the url to test different repo
url = 'https://api.github.com/repos/facebook/react/issues'
# you can change/add query to test any available filter -- &labels:bug
query = '?q=state:open'
# your github user name
username = 'ismaeluyghur'
# your github access token
token = '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'

request_util.get_issue_has_pull_request(url, query,  username, token)