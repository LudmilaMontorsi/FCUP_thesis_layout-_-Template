import requests
import json
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# First, find the correct PMC ID for Roberts et al. 2021 NMI paper
# DOI: 10.1038/s42256-021-00307-0
search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
params = {
    "db": "pmc",
    "term": "Roberts[Author] AND pitfalls machine learning COVID-19 chest radiographs CT scans[Title]",
    "retmode": "json",
    "retmax": 5
}
r = requests.get(search_url, params=params, headers=headers, timeout=30)
print("Search Status:", r.status_code)
if r.status_code == 200:
    data = r.json()
    print("IDs found:", data.get('esearchresult', {}).get('idlist', []))
    print()

time.sleep(2)

# Also search for the Oner et al. paper
params2 = {
    "db": "pmc",
    "term": "Oner[Author] AND patient level data segregation machine learning clinical",
    "retmode": "json",
    "retmax": 5
}
r2 = requests.get(search_url, params=params2, headers=headers, timeout=30)
print("Search Status (Oner):", r2.status_code)
if r2.status_code == 200:
    data2 = r2.json()
    print("IDs found:", data2.get('esearchresult', {}).get('idlist', []))
