import requests
import fitz

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

url = "https://www.medrxiv.org/content/10.1101/2020.04.23.20076406v1.full.pdf"
r = requests.get(url, headers=headers, timeout=30)
doc = fitz.open(stream=r.content, filetype='pdf')

# Print pages 2-7 with ASCII encoding
for page_num in range(1, 8):
    if page_num < len(doc):
        text = doc[page_num].get_text()
        text = text.encode('ascii', 'ignore').decode('ascii')
        print(f"=== PAGE {page_num+1} ===")
        print(text)
        print()
