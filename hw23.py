import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    html = codecs.open(html_file, 'r', 'utf-8').read()
    cleaned_text = re.sub('<[^>]*>', '', html)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)
