import re
import sys
import os
from bs4 import BeautifulSoup
import minify_html


def convert_pdf_to_html(pdf_file_path, html_folder):
    os.system(f'mkdir .{html_folder}')
    os.system(
        f'pdftohtml -c -noframes {pdf_file_path} .{html_folder}/{html_folder}.html')


def hydrate_html_with_bionic(html_folder):
    with open(f'.{html_folder}/{html_folder}.html', "rb") as original_file:
        soup = BeautifulSoup(original_file, 'html.parser')
        spans = soup.find_all('span')
        for span in spans:
            words = span.get_text().split()
            for i in range(len(words)):
                if re.match(r'([a-z]|[A-Z])', words[i][0]) != None:
                    middle = len(words[i]) // 2
                    if middle == 0 and len(words[i]) == 1:
                        middle = 1
                    words[i] = f'<strong>{words[i][:middle]}</strong>{words[i][middle:]}</span>'
            new_text = " ".join(words)
            span.string = ""
            tmp = BeautifulSoup(new_text, 'html.parser')
            span.append(tmp)

        minified = minify_html.minify(
            code=soup.prettify(), remove_processing_instructions=True)
        minified = re.sub(r'(\s<\/strong>\s)', '</strong>', minified)
        minified = minified.replace('#A0A0A0', '#ffffff', 1)
        with open(f'.{html_folder}/{html_folder}_hydrated.html', "wb") as f_output:
            f_output.write(minified.encode('utf-8'))


def convert_html_to_pdf(html_folder):
    os.system(
        f'wkhtmltopdf -T 0 -B 0 -L 0 -R 0 --enable-local-file-access --zoom 1.2 .{html_folder}/{html_folder}_hydrated.html {html_folder}_bionic.pdf')


def convert_pdf(filename):
    html_folder = filename.split('.')[0]
    convert_pdf_to_html(filename, html_folder)
    hydrate_html_with_bionic(html_folder)
    convert_html_to_pdf(html_folder)


if __name__ == '__main__':
    args = sys.argv[1:]
    convert_pdf(args[0])
