import requests
import fitz
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Oner et al. 2020 paper - DOI 10.1101/2020.04.23.20076406
# This is a medRxiv preprint

urls = [
    "https://www.medrxiv.org/content/10.1101/2020.04.23.20076406v1.full.pdf",
    "https://www.medrxiv.org/content/10.1101/2020.04.23.20076406v2.full.pdf",
    "https://www.medrxiv.org/content/10.1101/2020.04.23.20076406.full.pdf",
    # Also try europepmc PDF
    "https://europepmc.org/backend/ptpmcrender.fcgi?accid=PPR154143&blobtype=pdf",
]

for url in urls:
    try:
        r = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
        ct = r.headers.get('content-type', '')
        print(f"URL: {url[:60]}")
        print(f"Status: {r.status_code}, CT: {ct[:50]}")
        if r.status_code == 200 and 'pdf' in ct.lower():
            print("PDF FOUND! Size:", len(r.content))
            doc = fitz.open(stream=r.content, filetype='pdf')
            print("Pages:", len(doc))
            # Print first page
            print("=== FIRST PAGE ===")
            print(doc[0].get_text()[:1500])
        print()
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(2)
