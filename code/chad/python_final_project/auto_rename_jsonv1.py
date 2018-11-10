import os, PyPDF2, time, json
print(f'You Started with {len(os.listdir())}')
#Top Level variable to grab files that did not get renamed and ones that were renamed to lated be listed
matches_found = []
match_notfound = []

# Function To keyword Map which contains all info to rename file
def keyword_map():
    with open('rules.json') as rulefile:
        rules = json.load(rulefile)
    return rules
    
# Open Pdf and extract useful data
def open_pdf(file_name,):
    #Had to resort to this way because the with open did not work
    os.chdir('/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/doc_send')
    f = open(file_name, 'rb')
    pdfread = PyPDF2.PdfFileReader(f)
    f.close
    return pdfread
       
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
def auto_rename(pypdf2_file, file, finalname_list):
    #Variable that date slices go into
    final_date = ''
    #pypdf2 file gets passed into function and opened here to extract creation date
    date = pypdf2_file.getDocumentInfo()['/CreationDate']
    #Slice the main date part
    date = date[2:12]
    #concatinate final_date string with slices of above slice
    final_date += date[0:4] + '-' + date[4:6] + '-' + date[6:8] + '-' + date[8:10]

    final_filename = final_date + ' - ' + ''.join(finalname_list[0])
    print(final_filename)
    os.rename(file, final_filename)
    print(f'You ended with {print(os.listdir())} files')

def find_matchL1(opened_file):
    for keyword in keyword_map:
            if keyword in opened_file:
                return (keyword_map[keyword])

def find_matchL2(opened_file, keyword_map):
    for keyword in keyword_map['l2keywords']:
        if keyword in opened_file:
            return (keyword_map['l2keywords'][keyword])
            #print(f'you found L2 match{keyword_map[keyword]}')

def run_renameL1(keyword_map):
    # Change source directory where files will be renamed from
    source_directory = 'doc_send/'
    # Change target directory where renamed files will be moved to
    target_directory = 'doc_receive/'
    enum_folder = os.listdir(source_directory)
    
    for file in enum_folder:
        finalname_list = []
        #extract OCR data and return to match with keywords:
        pypdf2_file = open_pdf(file)
        opened_file = pypdf2_file.getPage(0).extractText()
        #call level one function to match first level keyword with ocrdata
        found_matchL1  = find_matchL1(opened_file)
        #if keyword matches True then
        if found_matchL1 is not None:
            #See if there is a L2 keyword to match
            found_matchL2 = find_matchL2(opened_file, found_matchL1)
            if found_matchL2 is not None:
                #if L2 keyword matches then create a list with the Type - Name - Keyword - L2Keyword
                #Call file rename function
                finalname_list.append([found_matchL1['type'], ' - ',
                found_matchL1['prettyname'], ' - ', 
                found_matchL2,
                '.pdf'])
                auto_rename(pypdf2_file, file, finalname_list)
            elif found_matchL2 is None:
                ##If no L2 Keyword is found rename the file wihtout a L2keyword
                #call file rename function
                # I would like to add a function to add rules and rerun to get the second match
                finalname_list.append([found_matchL1['type'], ' - ',
                found_matchL1['prettyname'],
                '.pdf'])
                auto_rename(pypdf2_file, file, finalname_list)
      
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

#Run First Level Rename Processes
ran_renameL1 = run_renameL1(keyword_map)

#Tell user about files that did and did not match keywords
#matches_notfound(match_notfound, matches_found)


#Here is some help with the json dictionary
# print(rules.keys()) # Level 1 is keywords
# print(rules['northwes']['l2keywords']) #Level 2 keywords
# print(rules['northwes']['l2keywords']['4plex']) # Level 2 Pretty Name
# print(rules['prettyname']['type'])