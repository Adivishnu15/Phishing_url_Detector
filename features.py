# features.py
import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    # IsDomainIP
    features.append(1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0)

    # URLLength
    features.append(len(url))

    # HasObfuscation (simple check for encoding, %, @, etc.)
    features.append(1 if re.search(r"%|@|\\x|\\u", url) else 0)

    # IsHTTPS
    features.append(1 if url.lower().startswith("https") else 0)

    # NoOfSubDomain
    netloc = urlparse(url).netloc
    features.append(len(netloc.split(".")) - 1)

    # HasSocialNet
    features.append(1 if re.search(r"facebook|twitter|instagram|linkedin", url) else 0)

    # NoOfURLRedirect (basic detection via multiple `//`)
    features.append(url.count('//') - 1)

    return features
