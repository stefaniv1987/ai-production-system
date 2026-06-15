import requests
from typing import Dict, Any


class JiraAdapter:
    """
    MCP adapter for interacting with Jira safely.
    """

    def __init__(self, base_url: str, api_token: str):
        self.base_url = base_url
        self.api_token = api_token

    def get_issue(self, issue_key: str) -> Dict[str, Any]:
        """
        Retrieves information for a Jira issue.
        """

        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Accept": "application/json"
        }

        url = f"{self.base_url}/rest/api/3/issue/{issue_key}"

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()

        return {
            "error": f"Unable to retrieve issue {issue_key}"
        }
