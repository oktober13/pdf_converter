import PyPDF2
import textract
import pdfplumber

def extract_text_with_pypdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        extracted_text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()

        return extracted_text


def extract_text_with_textract(pdf_path):
    text = textract.process(pdf_path)
    return text.decode('utf-8')


def extract_text_with_pdfplumber(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        extracted_text = ""
        for page in pdf.pages:
            extracted_text += page.extract_text()

        return extracted_text


def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


def main():
    # Ввод адреса PDF-документа
    pdf_path = input("Введите адрес PDF-документа: ")

    # Извлечение текста с использованием PyPDF2
    extracted_text_pypdf = extract_text_with_pypdf(pdf_path)
    txt_path_pypdf = pdf_path.replace('.pdf', '_pypdf.txt')
    save_text_to_file(extracted_text_pypdf, txt_path_pypdf)
    print(f"Текст, извлеченный с помощью PyPDF2, успешно сохранен в файле: {txt_path_pypdf}")

    # Извлечение текста с использованием textract
    extracted_text_textract = extract_text_with_textract(pdf_path)
    txt_path_textract = pdf_path.replace('.pdf', '_textract.txt')
    save_text_to_file(extracted_text_textract, txt_path_textract)
    print(f"Текст, извлеченный с помощью textract, успешно сохранен в файле: {txt_path_textract}")

    # Извлечение текста с использованием pdfplumber
    extracted_text_pdfplumber = extract_text_with_pdfplumber(pdf_path)
    txt_path_pdfplumber = pdf_path.replace('.pdf', '_pdfplumber.txt')
    save_text_to_file(extracted_text_pdfplumber, txt_path_pdfplumber)
    print(f"Текст, извлеченный с помощью pdfplumber, успешно сохранен в файле: {txt_path_pdfplumber}")


if __name__ == '__main__':
    main()