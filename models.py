# Create a Chunk data strcuture that contains
# the unique chunk_id,
# the page number,
# the text of the chunk,
# the start and end character indices of the chunk in the page text.
from dataclasses import dataclass


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    pdf_page: int
    text: str
    start_char: int
    end_char: int
