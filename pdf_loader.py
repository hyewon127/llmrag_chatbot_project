from pypdf import PdfReader

def load_pdf(path):

    reader = PdfReader(path)

    text = ""

    for page in reader.pages:

        text += page.extract_text()

    return text


#테스트 코드
if __name__ == "__main__":

    text = load_pdf(
        "네트워크 중간고사 정리.pdf"
    )

    print(text)
