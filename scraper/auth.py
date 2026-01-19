import requests

def get_session():
    session = requests.Session()

    # Simulated auth headers (internal site example)
    session.headers.update({
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html"
    })

    return session
