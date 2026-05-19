import requests
import fitz

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Got the PDF! Now read the full content
url = "https://www.medrxiv.org/content/10.1101/2020.04.23.20076406v1.full.pdf"
r = requests.get(url, headers=headers, timeout=30)
doc = fitz.open(stream=r.content, filetype='pdf')

print(f"Pages: {len(doc)}")
print()

# Print all pages to find the key passages
for page_num in range(len(doc)):
    text = doc[page_num].get_text()
    print(f"=== PAGE {page_num+1} ===")
    print(text)
    print()
