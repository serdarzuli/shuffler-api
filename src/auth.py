import ssl
from src.config import CERT_PATH, KEY_PATH

def get_ssl_context():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ssl_context.load_cert_chain(CERT_PATH, KEY_PATH)
    return ssl_context

def get_headers(token: str):
       
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }