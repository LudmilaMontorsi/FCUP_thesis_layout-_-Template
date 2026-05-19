import requests, fitz, io

# Try Oner et al. 2020 - patient level data segregation
urls = [
    'https://www.biorxiv.org/content/10.1101/2020.03.05.979526v1.full.pdf',
    'https://www.biorxiv.org/content/10.1101/2020.04.06.027797v1.full.pdf',
    'https://www.biorxiv.org/content/10.1101/2020.04.06.027797v2.full.pdf',
    'https://www.biorxiv.org/content/10.1101/2020.04.14.039727v1.full.pdf',
]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for url in urls:
    try:
        r = requests.get(url, headers=headers, timeout=15)
        ct = r.headers.get('content-type', '')
        print('URL:', url)
        print('Status:', r.status_code, 'CT:', ct)
        if r.status_code == 200 and 'pdf' in ct:
            doc = fitz.open(stream=r.content, filetype='pdf')
            first_page = doc[0].get_text()
            print(first_page[:500])
        print()
    except Exception as e:
        print('Error:', e)
