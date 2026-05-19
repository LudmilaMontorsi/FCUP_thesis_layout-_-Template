import requests
import fitz
import sys

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

url = "https://www.medrxiv.org/content/10.1101/2020.04.23.20076406v1.full.pdf"
r = requests.get(url, headers=headers, timeout=30)
doc = fitz.open(stream=r.content, filetype='pdf')

# Search for key passages
keywords = ['same patient', 'patient-level', 'patient level', 'inflate', 'inflat', 
            'overestim', 'overfit', 'data leakage', 'data leak', 'overlap', 
            'train.*test', 'segregat']

import re

output_lines = []
for page_num in range(len(doc)):
    text = doc[page_num].get_text()
    # Replace problematic chars
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    for kw in keywords:
        try:
            if re.search(kw, text, re.IGNORECASE):
                matches = list(re.finditer(kw, text, re.IGNORECASE))
                for m in matches[:2]:
                    start = max(0, m.start()-200)
                    end = min(len(text), m.end()+400)
                    context = text[start:end]
                    output_lines.append(f"--- Page {page_num+1}, keyword [{kw}] ---")
                    output_lines.append(context.strip())
                    output_lines.append("")
        except:
            pass

with open('scripts/oner_passages.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("Done! Found", len(output_lines), "lines")
