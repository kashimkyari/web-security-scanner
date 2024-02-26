# vulnerabilities.py
import re

def detect_vulnerabilities(soup):
    vulnerabilities = []

    # Detect SQL injection vulnerabilities
    sql_injection_vulnerabilities = detect_sql_injection(soup)
    vulnerabilities.extend(sql_injection_vulnerabilities)

    # Detect XSS vulnerabilities
    xss_vulnerabilities = detect_xss(soup)
    vulnerabilities.extend(xss_vulnerabilities)

    # Add more vulnerability detection functions as needed

    return vulnerabilities

def detect_sql_injection(soup):
    # Placeholder function for detecting SQL injection vulnerabilities
    # Example: Look for SQL-related keywords in HTML content
    sql_keywords = ['select', 'insert', 'update', 'delete', 'drop', 'alter', 'truncate']
    detected_vulnerabilities = []
    for tag in soup.find_all():
        for attr in tag.attrs.values():
            for value in attr:
                if any(keyword in value.lower() for keyword in sql_keywords):
                    detected_vulnerabilities.append({
                        'type': 'SQL Injection',
                        'location': tag.name,
                        'value': value
                    })
    return detected_vulnerabilities

def detect_xss(soup):
    # Placeholder function for detecting XSS vulnerabilities
    # Example: Look for script tags and event attributes in HTML content
    detected_vulnerabilities = []
    script_tags = soup.find_all('script')
    event_attributes = ['onmouseover', 'onerror', 'onload', 'onclick', 'onsubmit', 'onkeydown']
    for tag in script_tags:
        detected_vulnerabilities.append({
            'type': 'XSS',
            'location': 'script tag',
            'value': str(tag)
        })
    for attr in event_attributes:
        tags_with_event_attr = soup.find_all(attrs={re.compile(attr): True})
        for tag in tags_with_event_attr:
            detected_vulnerabilities.append({
                'type': 'XSS',
                'location': tag.name,
                'value': str(tag)
            })
    return detected_vulnerabilities
