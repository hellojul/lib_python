# pip install PyPDF2 pdfplumber
import PyPDF2
import pdfplumber

# Fonction pour extraire le texte d'un fichier PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

# Fonction pour extraire les métadonnées d'un PDF
def extract_metadata_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        metadata = reader.metadata
        return metadata

# Fonction pour extraire des images d'un PDF
def extract_images_from_pdf(pdf_path, output_folder):
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            if 'images' in page:
                for j, img in enumerate(page.images):
                    img_path = f"{output_folder}/image_{i}_{j}.png"
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img['stream'])

# Fonction pour fusionner plusieurs fichiers PDF
def merge_pdfs(pdf_paths, output_path):
    merger = PyPDF2.PdfWriter()
    for pdf_path in pdf_paths:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                merger.add_page(reader.pages[page_num])
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

# Fonction pour extraire une page spécifique d'un PDF
def extract_page_from_pdf(pdf_path, page_number, output_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()
        writer.add_page(reader.pages[page_number])
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# Fonction pour diviser un PDF en plusieurs fichiers (une page par fichier)
def split_pdf(pdf_path, output_folder):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_num])
            output_path = f"{output_folder}/page_{page_num+1}.pdf"
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

# Fonction pour ajouter un filigrane à un PDF
def add_watermark(pdf_path, watermark_path, output_path):
    with open(pdf_path, 'rb') as pdf_file, open(watermark_path, 'rb') as watermark_file:
        reader = PyPDF2.PdfReader(pdf_file)
        watermark_reader = PyPDF2.PdfReader(watermark_file)
        writer = PyPDF2.PdfWriter()

        watermark_page = watermark_reader.pages[0]

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page.merge_page(watermark_page)
            writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

