import os, PyPDF2, time

#Top Level variable to grab files that did not get renamed and ones that were renamed to lated be listed
matches_found = []
match_notfound = []

# Function To keyword Map which contains all info to rename file
def keyword_map():
    with open('__keyword_Filepointer.csv', 'r') as keywords:
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
def open_pdf(source_dir, file_name,):
    #Had to resort to this way because the with open did not work
    print(os.getcwd())
    f = open(source_dir+file_name, 'rb')
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
    os.rename(src, dst)
    # os.rename(file_formated)

def run_rename():
    # Change source directory where files will be renamed from
    source_directory = '/Users/chadbean/Documents/Programing and Development/github/class_redmage/code/chad/python_final_project/doc_send/'
    # Change target directory where renamed files will be moved to
    target_directory = '/Users/chadbean/Documents/Programing and Development/github/class_redmage/code/chad/python_final_project/doc_receive/'
    enum_folder = os.listdir(source_directory)
    
    for filename in enum_folder:
        print(filename)
    # Call func and open pdf file, return variable containing all the ocr information needed
        opened_pdf = open_pdf(source_directory, filename)
        #Compare ocr data with keywords to match
        found_match = find_matches(made_dict, opened_pdf)
        #Use matched data to generate file format for autorename function, if/else:
        # To see if found_match returns None, if None continue
        if found_match is None:
            match_notfound.append(filename)
            continue
        else:
            matches_found.append(filename)
            file_formated = file_format(found_match, opened_pdf)
            print(file_formated)
        #Send file_formated into function to do actual file rename
        auto_renamed = auto_rename(file_formated,filename, source_directory, target_directory)

def matches_notfound(matches_not_found, matches_found):
    print('\n\nThe Following Files Did Match!!')
    for match in matches_found:
        print(match)
    time.sleep(2)
    print('\n\nThe Following Files Did Not Find Any Matches. You Will Either Have To Be Manually Renamed Or New Renaming Rule Created:\n')
    for match in matches_not_found:
        print(match)
    time.sleep(2)

   
#Open keyword csv and parse/split into a dictionary with key being the company.
#This will be used for the autorename and file move functions
keyword_map = keyword_map()
made_dict = make_dict(keyword_map)

#Run First Level Rename Processes
run_rename()

#Tell user about files that did and did not match keywords
matches_notfound(match_notfound, matches_found)