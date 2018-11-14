from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import string

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
file = convert_pdf_to_txt('/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/doc_send/2015-05-31-11 - Bill - Northwest Energy - 2520 Larkinwood Dr.pdf')


file_list = []

file = file.split()
file = list(file)
for i in file:
    file_list.append((file.count(i),i))

# sorted(file_list,)
file_list = set(file_list)
file_list = sorted(file_list)

for file in file_list[-1:-11:-1]:
    print(file)