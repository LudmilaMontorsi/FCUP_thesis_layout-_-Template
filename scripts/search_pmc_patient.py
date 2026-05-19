import requests
import time
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Search for papers about patient-level splitting and its effect on performance inflation in medical imaging
searches = [
    "patient level split inflated performance deep learning medical imaging CT MRI",
    "same patient train test overestimated accuracy medical imaging deep learning",
    "data leakage patient overlap train test set medical imaging radiology deep learning",
    "patient level data split overoptimistic deep learning radiology",
]

for term in searches:
    params = {
        "db": "pmc",
        "term": term,
        "retmode": "json",
        "retmax": 5
    }
    r = requests.get(search_url, params=params, headers=headers, timeout=30)
    if r.status_code == 200:
        data = r.json()
        ids = data.get('esearchresult', {}).get('idlist', [])
        print(f"Query: {term[:60]}...")
        print(f"IDs: {ids}")
        print()
    time.sleep(1)
