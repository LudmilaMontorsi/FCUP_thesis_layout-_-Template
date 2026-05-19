import requests
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# Search for Roberts 2021 Nature Machine Intelligence paper
searches = [
    {
        "db": "pubmed",
        "term": "Roberts[Author] AND common pitfalls recommendations machine learning COVID-19 chest radiographs",
        "retmode": "json", "retmax": 5
    },
    {
        "db": "pubmed",
        "term": "10.1038/s42256-021-00307-0[doi]",
        "retmode": "json", "retmax": 5
    },
    {
        "db": "pmc",
        "term": "common pitfalls machine learning COVID-19 CT scans radiographs patient overlap data leakage",
        "retmode": "json", "retmax": 5
    }
]

for params in searches:
    r = requests.get(search_url, params=params, headers=headers, timeout=30)
    print(f"Search ({params['term'][:60]}...):")
    print("Status:", r.status_code)
    if r.status_code == 200:
        data = r.json()
        ids = data.get('esearchresult', {}).get('idlist', [])
        print("IDs:", ids)
    print()
    time.sleep(1)
