import requests, fitz, io

# Search for Oner et al. 2020 through Semantic Scholar API
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Try semantic scholar search API
url = "https://api.semanticscholar.org/graph/v1/paper/search"
params = {
    "query": "Training machine learning models patient level data segregation crucial clinical applications",
    "fields": "title,abstract,year,authors,externalIds,openAccessPdf",
    "limit": 5
}
r = requests.get(url, params=params, headers=headers, timeout=30)
print("Status:", r.status_code)
if r.status_code == 200:
    import json
    data = r.json()
    for paper in data.get('data', []):
        print("Title:", paper.get('title'))
        print("Year:", paper.get('year'))
        print("Authors:", [a.get('name') for a in paper.get('authors', [])])
        print("Abstract:", paper.get('abstract', '')[:400])
        print("openAccessPdf:", paper.get('openAccessPdf'))
        print("externalIds:", paper.get('externalIds'))
        print()
