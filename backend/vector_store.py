import chromadb
from pypdf import PdfReader

# Read PDF
pdf_path = "uploads/Text_to_PDF_Onlinenotpad-3.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text


# Split text into chunks
def split_text(text, chunk_size=600):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


chunks = split_text(text)

# ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_store"
)

collection = client.get_or_create_collection(
    name="documents"
)

# Store chunks
for i, chunk in enumerate(chunks):

    collection.add(
        ids=[str(i)],
        documents=[chunk]
    )

print("Stored", len(chunks), "chunks")