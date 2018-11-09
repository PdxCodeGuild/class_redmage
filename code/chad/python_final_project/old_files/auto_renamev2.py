import sys, PyPDF2, re, json, os

# We load a JSON file that contains the rules we have defined
# The json file contains a data structure.

# The keys in the dict are the "Company Names"
# For the key, if we find it in the text
# We evaluate the rules associated with the key
# The rules are named extract, and they are regexes
# defining what we want to extract out of the string
# the key for each regex is the variable name to be used
# as part of the filename. For example, if the key is 
# customer_name and the regex is "customer: (.*?),foo"
# then the template variable customer_name will contain
# whatever was in the parenthesis in the regex, and can
# then be used in the filename...
# assume the PDF contains 'customer: Chad Bean,foo', then
# customer_name would be 'Chad Bean' and if the file format
# was customer_name.txt it would be 'Chad Bean.txt'



def open_and_extract(file):
    os.chdir('..')
    os.chdir('doc_send')
    f = open(file, 'rb')
    pdfread = PyPDF2.PdfFileReader(file)
    text = pdfread.getPage(0).extractText()
    text = text.lower()
    f.close()
    return text
    

def find_matches(file, ocr_text):
    #Open Json rules
    #ocr_text = ocr_text.lower()
    os.chdir('..')
    os.chdir('rules')
    with open('rules.json') as f:
        rules = json.load(f)
#{'Northwestern Energy': {'extract': {'saddress': 'Service Address: (.*?),', 'acct': '([\\d\\-]+?)CUSTOMER:ACCOUNT NUMBER'}, 'format': 'date-saddress-acct', 'dir': 'nwenergy'}}
# For each rule such as Northwest Energy
# (key)
    for k in rules.keys(): 
        if k in ocr_text:
            #print(f'found {k}')
            for v in rules[k]['extract'].values():
                #print(v)
                p = re.compile(v)
                m = p.search(ocr_text)
                if m:
                    print(m.group(1))
                    

def loop_through_files():
    os.chdir('doc_send')
    dir_files = os.listdir()
    for file in dir_files:
        ocr_text = open_and_extract(file)
        find_matches(file, ocr_text)
    
loop_through_files()
