import streamlit as st
import pymupdf

def main():
    st.title("Datasheet Assistant")
    # upload a pdf file
    uploaded_file = st.file_uploader("Choose a PDF", type=["pdf"])
    if uploaded_file is None:
        return

    # open the file with pymupdf
    pdf = pymupdf.open(stream=uploaded_file.getvalue(), filetype="pdf")
    # get the page count
    page_count = pdf.page_count
    # select a page number
    page_number = st.number_input(
        "Page number",
        min_value=1,
        max_value=page_count,
        value=1,
        step=1,
    )
    # get the page
    page = pdf[page_number - 1]
    # get the page image
    pixmap = page.get_pixmap(matrix=pymupdf.Matrix(2, 2))
    st.image(pixmap.tobytes("png"), caption=f"Page {page_number} of {page_count}")
    st.subheader("Page text")
    text = page.get_text().strip()
    st.text(text or "(No extractable text on this page)")


if __name__ == "__main__":
    main()
