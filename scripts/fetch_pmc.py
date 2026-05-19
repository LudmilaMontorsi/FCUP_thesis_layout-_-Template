import requests
import json
import time
import fitz

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Fetch details for the found PMC IDs from Oner search
pmc_ids = ['11595419', '11339347', '9879258', '9768677', '8848022']

fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

for pmcid in pmc_ids:
    params = {
        "db": "pmc",
        "id": pmcid,
        "retmode": "xml",
        "rettype": "abstract"
    }
    r = requests.get(fetch_url, params=params, headers=headers, timeout=30)
    if r.status_code == 200:
        # Extract title and abstract from XML
        text = r.text
        # Get title
        title_start = text.find('<article-title>')
        title_end = text.find('</article-title>')
        if title_start != -1:
            title = text[title_start+15:title_end][:200]
            print(f"PMC{pmcid}: {title}")
        
        # Get abstract
        abs_start = text.find('<abstract>')
        abs_end = text.find('</abstract>')
        if abs_start != -1:
            abstract = text[abs_start+10:abs_end][:400]
            print(f"Abstract: {abstract[:300]}")
        print()
    time.sleep(1)
