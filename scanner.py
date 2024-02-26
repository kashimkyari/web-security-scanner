# scanner.py
import requests
from bs4 import BeautifulSoup
from vulnerabilities import detect_vulnerabilities

class WebScanner:
    def __init__(self):
        pass

    def scan(self, url):
        try:
            # Fetch webpage content
            response = requests.get(url)
            if response.status_code == 200:
                html_content = response.text
            else:
                return {'error': 'Failed to fetch webpage'}
        except requests.RequestException as e:
            return {'error': str(e)}

        try:
            # Parse HTML content
            soup = BeautifulSoup(html_content, 'html.parser')
        except Exception as e:
            return {'error': 'Failed to parse HTML content'}

        # Detect vulnerabilities
        vulnerabilities = detect_vulnerabilities(soup)

        return vulnerabilities
