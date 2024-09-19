import json
import os

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.parametrize(
    'repo_name',
    (
            ['test_api_repo']
    )
)
def test_api(repo_name: str) -> None:
    headers = {'Authorization': 'token ' + os.getenv('TOKEN')}
    params = json.dumps({'name': repo_name})
    response = requests.post(url='https://api.github.com/user/repos', data=params, headers=headers)
    assert response.status_code == 201
    response = requests.get(url=f'https://api.github.com/repos/{os.getenv('USER')}/{repo_name}', headers=headers)
    assert response.status_code == 200
    assert response.json().get('name') == repo_name
    response = requests.delete(f'https://api.github.com/repos/{os.getenv('USER')}/{repo_name}', headers=headers)
    assert response.status_code == 204
