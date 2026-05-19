import requests, fitz, io
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Try Roberts et al. 2021 - Nature Machine Intelligence - Common pitfalls COVID-19 CT
# DOI: 10.1038/s42256-021-00307-0
# This paper explicitly lists patient overlap as a pitfall

# Try the PMC version (should be freely accessible since it's CC-BY)
# PMC ID for Roberts et al. 2021 NMI is PMC8236064
urls_to_try = [
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC8236064/pdf/",
    "https://europepmc.org/backend/ptpmcrender.fcgi?accid=PMC8236064&blobtype=pdf",
]

for url in urls_to_try:
    try:
        r = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
        ct = r.headers.get('content-type', '')
        print("URL:", url[:60])
        print("Status:", r.status_code, "CT:", ct[:50])
        print()
    except Exception as e:
        print("Error:", e)
    time.sleep(2)
