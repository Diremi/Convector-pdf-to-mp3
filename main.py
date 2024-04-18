from pdfplumber import open as pdf_open
from gtts import gTTS
from os import mkdir
from os.path import splitext, basename, exists
from shutil import move


def get_PDF_text(path: str) -> str:
    with pdf_open(path) as PDF:
        text = ''
        for page in PDF.pages:
            text = text + page.extract_text()
    
    return text
 
def PDF_to_mp3(path: str, file_language: str):
    text = gTTS(get_PDF_text(path), lang=file_language)
    filename = splitext(basename(path))[0]
    text.save(filename + '.mp3')

    if not exists('MP3'):
        mkdir('MP3')
    else:
        move(filename + '.mp3', 'MP3')



PDF_file_path = input('Введите путь до PDF файла: ')
file_language = input('Введите язык текста из файла (например: "ru"): ')

PDF_to_mp3(PDF_file_path, file_language)
