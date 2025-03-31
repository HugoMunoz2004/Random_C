import requests
import os
import datetime

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "NOM_DEL_USUARI"
REPO_NAME = "Random_C"
TAG = datetime.datetime.now().strftime("v%Y%m%d%H%M%S")

headers = {"Authorization": f"token {GITHUB_TOKEN}"}
data = {"tag_name": TAG, "name": TAG, "body": "Release automàtica"}
url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases"

response = requests.post(url, json=data, headers=headers)
print(response.json())
