import requests

url = "https://medium.com/"
result = requests.get(url)

file_path = "ProjectDocuments/results.html"

with open(file_path, "w") as fin:
    fin.write(str(result.content))

'''try to login on a site'''
url = "https://medium.com/"
payload = {'inUserName': 'USERNAME/EMAIL', 'inUserPass': 'PASSWORD'}