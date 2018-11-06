import os, datetime, PyPDF2

print(f'You Are Working In A {os.name} EnVironment')

#Ask User To Set The Path Where PDFs Are Stored:
#path_input = input('What Path Are The PDFs Stored That You Would Like To Rename? > ')
path_input = '/tmp/'

# Function To keyword Map
def keyword_map():
    with open('/tmp/doc_send/keywords.csv', 'r') as keywords:
        keyword_map = keywords.read().strip('\n').split('\n')
    keywords.close()
    return keyword_map

# Parse key_map into dictionary
def make_dict(keyword_map):
    final_listOfDic = []
    make_list = []

    # Loop over each index and split each index into a list
    for eachindex in keyword_map:
        make_list.append(eachindex.split(','))
    # Loop over each index and make a dictionary from each
    for eachindex in make_list:
        final_listOfDic.append({eachindex[0]:(eachindex[1], eachindex[2])})
    return final_listOfDic
    
# Open Pdf and extract useful data
def open_pdf():
    # with open('/tmp/doc_send/nwebill.pdf', 'rb') as pdf:
    #     pdfread = PyPDF2.PdfFileReader(pdf)
    # return pdfread

    f = open('/tmp/doc_send/nwebill.pdf', 'rb')
    pdfread = PyPDF2.PdfFileReader(f)
    f.close
    return pdfread

def find_matches(keywords, ocrdata):
    #Extract ocr text from ocrdata
    page = ocrdata.getPage(0)
    print(page)
    

#Open keyword csv and split into a dictionary with key being the company.
#This will be used for the autorename and file move functions
keyword_map = keyword_map()
make_dict = make_dict(keyword_map)

#Open pdf file and return variable containing all the ocr information needed
open_pdf = open_pdf()

#Compare ocr data with keywords to match
find_matches = find_matches(keyword_map, open_pdf)