import os
import requests
import zipfile

def download_and_extract_docs():
    token = os.environ.get('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'}
    api_url = 'https://api.github.com/repos/gavin/piqtree2/actions/runs'
    response = requests.get(api_url, headers=headers)
    got = response.json()
    print(got)
    runs = got['workflow_runs']
    latest_run = next(run for run in runs if run['name'] == 'Build docs' and run['conclusion'] == 'success')
    artifacts_url = latest_run['artifacts_url']
    response = requests.get(artifacts_url, headers=headers)
    artifacts = response.json()['artifacts']
    docs_artifact = next(artifact for artifact in artifacts if artifact['name'] == 'piqtree-docs-html')
    download_url = docs_artifact['archive_download_url']
    response = requests.get(download_url, headers=headers)
    with open('piqtree-docs-html.zip', 'wb') as f:
        f.write(response.content)
    with zipfile.ZipFile('piqtree-docs-html.zip', 'r') as zip_ref:
        zip_ref.extractall('_readthedocs/html/')

if __name__ == "__main__":
    download_and_extract_docs()
