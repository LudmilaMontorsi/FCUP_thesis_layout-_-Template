import requests
import time
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Search for Oner paper specifically through Europe PMC which indexes bioRxiv
url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
params = {
    "query": "Training machine learning models patient level data segregation crucial clinical applications Oner",
    "resultType": "core",
    "format": "json",
    "pageSize": 5
}
r = requests.get(url, params=params, headers=headers, timeout=30)
print("Status:", r.status_code)
if r.status_code == 200:
    import json
    data = r.json()
    results = data.get('resultList', {}).get('result', [])
    for item in results:
        print("Title:", item.get('title', ''))
        print("Authors:", item.get('authorString', ''))
        print("Year:", item.get('pubYear', ''))
        print("Source:", item.get('source', ''))
        print("DOI:", item.get('doi', ''))
        print("Abstract:", item.get('abstractText', '')[:300])
        print()
