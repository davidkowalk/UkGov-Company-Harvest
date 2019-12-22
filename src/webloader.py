from urllib.request import urlopen as ureq

def load(url):
    client = ureq(url)
    content = client.read()
    client.close()
    return content
