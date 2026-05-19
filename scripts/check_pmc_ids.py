import requests
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Check the PMC IDs from last search
pmc_ids = ['13072745', '12768402', '12714659', '12650584', '12560119']

for pmcid in pmc_ids:
    params = {
        "db": "pmc",
        "id": pmcid,
        "retmode": "xml",
    }
    r = requests.get(fetch_url, params=params, headers=headers, timeout=30)
    if r.status_code == 200:
        text = r.text
        title_start = text.find('<article-title>')
        title_end = text.find('</article-title>')
        title = text[title_start+15:title_end][:200] if title_start != -1 else "NO TITLE"
        
        # Check for patient overlap / patient level mentions
        keywords = ['patient overlap', 'patient-level', 'patient level', 'same patient', 'inflate', 'data leak']
        found = [kw for kw in keywords if kw.lower() in text.lower()]
        
        print(f"PMC{pmcid}: {title}")
        print(f"  Keywords found: {found}")
        
        # If relevant keywords found, show context
        for kw in found[:2]:
            idx = text.lower().find(kw.lower())
            if idx != -1:
                start = max(0, idx-200)
                end = min(len(text), idx+400)
                context = text[start:end].replace('<p>', '').replace('</p>', '').replace('<bold>', '').replace('</bold>', '')
                # Remove XML tags roughly
                import re
                context_clean = re.sub(r'<[^>]+>', '', context)
                print(f"  Context [{kw}]:", context_clean[:300])
        print()
    time.sleep(1)
