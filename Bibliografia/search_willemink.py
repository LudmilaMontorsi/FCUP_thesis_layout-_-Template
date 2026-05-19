import fitz

doc = fitz.open('31. Preparing Medical Imaging Data for Machine Learning - Willemink et al.pdf')
full_text = ''
for i, page in enumerate(doc):
    full_text += f'\n--- PAGE {i+1} ---\n' + page.get_text()

keywords = ['same patient', 'patient-level', 'patient level', 'inflate', 'optimistic', 'overestim', 'leakage', 'data leak', 'split', 'partition']
for kw in keywords:
    idx = 0
    count = 0
    while count < 3:
        idx = full_text.lower().find(kw.lower(), idx)
        if idx == -1:
            break
        print(f'[{kw}]:')
        print(full_text[max(0, idx-250):idx+500])
        print('---')
        idx += len(kw)
        count += 1
