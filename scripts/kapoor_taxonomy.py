import requests
import fitz

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

url = 'https://arxiv.org/pdf/2207.07048'
r = requests.get(url, headers=headers, timeout=60)
doc = fitz.open(stream=r.content, filetype='pdf')

# Print pages 3-9 (0-indexed: 2-8) to find the taxonomy of leakage types
for page_num in range(2, 10):
    text = doc[page_num].get_text()
    text_ascii = text.encode('ascii', 'ignore').decode('ascii')
    
    # Only print pages with relevant content
    relevant_kws = ['patient', 'non-independent', 'independence', 'no split', 'patient-level', 
                    'leakage type', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8',
                    'inflat', 'overfit', 'overestim']
    if any(kw.lower() in text_ascii.lower() for kw in relevant_kws):
        print(f"=== PAGE {page_num+1} ===")
        print(text_ascii[:3000])
        print()
