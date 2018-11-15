from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import collections
import os


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()
    return text


def run_compare_words(word_path):
    words = []
    final_word_str = ''
    for i in os.listdir(word_path):

        try:
            print(f'You Are Analyzing File {i}')
            if '.pdf' in i:
                text = convert_pdf_to_txt(word_path + i)
                for word in text.split("\n"):
                    words.append(word.lower())
        except:
            print('Program Threw Exception')
    #My Friend Dan Helped Me With This Function Of Using Collections
    word_count = collections.Counter(words)
    for word, count in word_count.most_common(100):
        final_word_str += ("{}, {}".format(word, count) + "\n")
    return final_word_str