import fitz, os

target_pdfs = [
    '1. Advancements in supervised deep learning for metal artifact reduction in computed tomography A systematic review.pdf',
    '31. Key challenges for delivering clinical impact with artificial intelligence - Kelly et al.pdf',
    '2. Enhancing CCTA image quality a review of deep learning approaches for advanced artifact correction and denoising.pdf',
    '3. Transforming CT imaging with deep learning Noise reduction, artifact management, and clinical applications - A comprehensive review.pdf',
    '6. Deep Learning Methods for CT Image-Domain Metal Artifact Reduction - Gjesteby et al.pdf',
    '18. Advances in metal artifact reduction in CT images - A review of current status and future directions - Selles et al.pdf',
]

for pdf in target_pdfs:
    if not os.path.exists(pdf):
        print(f'NOT FOUND: {pdf}')
        continue
    try:
        doc = fitz.open(pdf)
        full_text = ''.join(page.get_text() for page in doc)
        found = False
        for i in range(0, len(full_text) - 800, 50):
            window = full_text[i:i+800].lower()
            if 'patient' in window and ('train' in window or 'test' in window) and any(w in window for w in ['inflat', 'leak', 'overfit', 'same patient', 'overlap', 'bias', 'separate']):
                print(f'\n=== {pdf[:70]} ===')
                print(full_text[i:i+800])
                print()
                found = True
                break
        if not found:
            print(f'[no match] {pdf[:70]}')
    except Exception as e:
        print(f'Error: {e} -- {pdf}')
