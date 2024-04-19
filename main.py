from pdfplumber import open as pdf_open
from pathlib import Path
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
 
def PDF_to_mp3(file_path: str, file_language: str):
    if not exists(file_path):
        return f'Ошибка: некорректный путь'
    elif Path(file_path).suffix != '.pdf':
        return f'Ошибка: некорректное расширение'
    
    text = gTTS(get_PDF_text(file_path), lang=file_language)
    filename = splitext(basename(file_path))[0]

    print(f'>>> Конвертация файла: {filename}.pdf')
    print('>>> В процессе...')

    text.save(filename + '.mp3')

    if not exists('Audiotext'):
        mkdir('Audiotext')
    else:
        move(filename + '.mp3', 'Audiotext')
    return f'Файл {filename}.pdf был успешно конвертирован в "{filename}.mp3"!'

def main():
    PDF_file_path = input('Введите путь до PDF файла: ')
    file_language = input('Введите язык текста из файла (например: "ru"): ')

    print(PDF_to_mp3(PDF_file_path, file_language))

if __name__ == '__main__':
    main()