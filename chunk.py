
import clean

CHUNK_SIZE = 500
def chunk_fill(pages):
    list_chunks = []
    chunks = []
    current_chunk = 0
    for page in pages :
        ligne = clean.line_cleaning(page["text"])
        chunks = []
        current_chunk = 0
        for line in ligne :
            
            if current_chunk + len(line) <= CHUNK_SIZE:
                current_chunk += len(line)
                chunks.append(line)
            else:
                list_chunks.join(chunks)
                chunks = []
            if line == ligne[-1] :
                list_chunks.join(chunks)



        
    