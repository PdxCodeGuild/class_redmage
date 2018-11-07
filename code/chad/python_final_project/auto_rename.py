import os, datetime, PyPDF2

print(f'You Are Working In A {os.name} EnVironment')

# Function To keyword Map which contains all info to rename file
def keyword_map():
    with open('/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/keywords.csv', 'r') as keywords:
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
def open_pdf(file_name):
    # with open('/tmp/doc_send/nwebill.pdf', 'rb') as pdf:
    #     pdfread = PyPDF2.PdfFileReader(pdf)
    # return pdfread
    #Had to resort to this way because the with open did not work
    f = open(file_name, 'rb')
    pdfread = PyPDF2.PdfFileReader(f)
    f.close
    return pdfread

def find_matches(keywords, ocrdata):
    #[{'keyword': ('type', 'to_dir')}, {'Northwestern Energy': ('Bill', '/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/doc_receive')}]
    #Extract ocr text from ocrdata
#I might need to scan mulitple pages
    page = ocrdata.getPage(0)
    extract_text = page.extractText()
    extract_text = extract_text.lower()
    #For each dictionary in keywords
    for listindex in keywords:
        #For each keyword in dictionary
        for in_dict in listindex:
            #If key in dictionary (keyword) the extracted ocr text then return that whole dictionary
            if in_dict in extract_text:
                return listindex
       
def file_format(keyword_match, ocrdata):
    final_filename = ''
#Get Creation Date For Rename Function
    final_date = ''
    page = ocrdata.getDocumentInfo()
    date = (page['/CreationDate'])
    date = date[2:12]
#I added two more characters on the timestamp to avoid any duplicates
    final_date += date[0:4] + '-' + date[4:6] + '-' + date[6:8] + '-' + date[8:10]
#Get type for file in dictionary from keyword
    file_type = list(keyword_match.values())
    final_type = str((file_type[0][1]))
#Get company name for file in dictionary from keyword
    keyword_name = list(keyword_match.values())
    final_name = str((keyword_name[0][0]))
#Construct string together for file rename operation
    final_filename += final_date + ' - ' + final_type + ' - ' + final_name
    return final_filename

#Funciotn To Auto Rename File 
def auto_rename(file_formated, filename, source_dir, target_dir):
#Source of File To 
    src = source_dir + filename
    dst = target_dir
    dst += file_formated + '.pdf'
    print(src)
    print(dst)
    os.rename(src, dst)
    # os.rename(file_formated)

def menu():
    #source_directory = input('What is the source directory that you want to rename all pdfs? > ')
    source_directory = '/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/doc_send/'
    target_directory = '/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/doc_receive/'
    os.chdir(source_directory)
    enum_folder = os.listdir(source_directory)
    
    for filename in enum_folder:
        # Call func and open pdf file, return variable containing all the ocr information needed
        opened_pdf = open_pdf(filename)
        #Compare ocr data with keywords to match
        found_match = find_matches(made_dict, opened_pdf)
        #Use matched data to generate file format for autorename function, if/else:
        # To see if found_match returns None, if None continue
        if found_match is None:
            continue
        else:
            file_formated = file_format(found_match, opened_pdf)
            print(file_formated)
        #Send file_formated into function to do actual file rename
        auto_renamed = auto_rename(file_formated,filename, source_directory, target_directory)
   
#Open keyword csv and split into a dictionary with key being the company.
#This will be used for the autorename and file move functions
keyword_map = keyword_map()
made_dict = make_dict(keyword_map)

#Run Program
menu()