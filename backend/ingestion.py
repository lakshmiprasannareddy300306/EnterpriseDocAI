from pypdf import PdfReader

pdf_path = "uploads/Text_to_PDF_Onlinenotpad-3.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text


def split_text(text, chunk_size=600):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


chunks = split_text(text)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print("Length:", len(chunk))