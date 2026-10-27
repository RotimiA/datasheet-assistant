# Write a retrieval algorithm/function that:
# 1. Find word positions in each page's text
# 2. Take a window of up to 250 words
# 3. Slice the original text using those word positions
# 4. Move forward 200 words, preserving the 50-word overlap
# 5. Stop when the window reaches the page's end
# 6. Start fresh on a new page

import re

from models import Chunk, PageText

WORD_RE = re.compile(r"\S+")


def chunk_pages(
    pages: list[PageText],
    chunk_words: int = 250,
    overlap_words: int = 50,
) -> list[Chunk]:
    if chunk_words < 1:
        raise ValueError("chunk_words must be at least 1")
    if overlap_words < 0:
        raise ValueError("overlap_words must be at least 0")
    if overlap_words >= chunk_words:
        raise ValueError("overlap_words must be smaller than chunk_words")

    stride = chunk_words - overlap_words
    chunks: list[Chunk] = []

    for page in pages:
        words = list(WORD_RE.finditer(page.text))
        if not words:
            continue

        start = 0
        word_count = len(words)
        while start < word_count:
            end = min(start + chunk_words, word_count)
            start_char = words[start].start()
            end_char = words[end - 1].end()
            chunks.append(
                Chunk(
                    chunk_id=f"{page.pdf_page}:{start_char}:{end_char}",
                    pdf_page=page.pdf_page,
                    text=page.text[start_char:end_char],
                    start_char=start_char,
                    end_char=end_char,
                )
            )
            if end == word_count:
                break
            start += stride

    return chunks
