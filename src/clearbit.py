from json import loads as parse
import webloader
from urllib.parse import quote_plus as url

def autocomplete(name):
    try:
        http_name = url(name)
        content = webloader.load(f"https://autocomplete.clearbit.com/v1/companies/suggest?query={http_name}")
        json = parse(content)
        return json
    except:
        print("Error")
        return None
