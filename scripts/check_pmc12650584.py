import requests
import time
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Get more details from PMC12650584 - Cancer and Aging Biomarkers paper
pmcid = '12650584'
params = {
    "db": "pmc",
    "id": pmcid,
    "retmode": "xml",
}
r = requests.get(fetch_url, params=params, headers=headers, timeout=30)
if r.status_code == 200:
    text = r.text
    # Find all contexts around data leakage in 2D slices
    keywords = ['2D MRI slice', '2D slice', 'slice-based', 'patient-level', 'same patient', 'data leakage']
    for kw in keywords:
        idx = 0
        while True:
            idx = text.lower().find(kw.lower(), idx)
            if idx == -1:
                break
            start = max(0, idx-300)
            end = min(len(text), idx+500)
            context = text[start:end]
            context_clean = re.sub(r'<[^>]+>', '', context)
            print(f"--- [{kw}] ---")
            print(context_clean.strip()[:600])
            print()
            idx += len(kw)
