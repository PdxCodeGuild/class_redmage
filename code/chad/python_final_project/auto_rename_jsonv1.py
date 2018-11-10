import os, PyPDF2, time, json, random


#Top Level variable to grab files that did not get renamed and ones that were renamed to lated be listed
matches_found = []
match_notfound = []
date_num_counter = 1
# Function To keyword Map which contains all info to rename file
def keyword_map():
    with open('rules.json') as rulefile:
        rules = json.load(rulefile)
    return rules

# Open Pdf and extract useful data
def open_pdf(file_name,):
    #Had to resort to this way because the with open did not work
    os.chdir('/Users/chadbean/Documents/Programing and Development/github/class_redmage/code/chad/python_final_project/doc_send')
    f = open(file_name, 'rb')
    pdfread = PyPDF2.PdfFileReader(f)
    f.close
    return pdfread

#Function To Auto Rename File
def auto_rename(pypdf2_file, file, finalname_list):
    #Variable that date slices go into
    final_date = ''
    #pypdf2 file gets passed into function and opened here to extract creation date
    date = pypdf2_file.getDocumentInfo()['/CreationDate']
    print(date)
    #Slice the main date part
    date = date[2:18]
    #concatinate final_date string with slices of above slice and date up to second because of files being deleted
    #or overwritting because of the same date andkey matches
    final_date += date[0:4] + '-' + date[4:6] + '-' + date[6:8] + '-' + date[8:10] + '-' + date[10:12] + '-' + date[12:14]
    final_filename = final_date + ' - ' + ''.join(finalname_list[0])
    if final_filename in os.listdir():
        print(f'You Are Overwritting a File {final_filename}')

    print(f'this is the filename BEFORE {file}')

    os.rename(file, final_filename)
    print(f'this is the filename AFTER {final_filename}')

    #Add 1 to date_num_counter to eliminate duplicates
    date_num_counter += 1

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
    print(enum_folder)
    try_counter = 0
    except_counter = 0
    for file in enum_folder:
        #Make sure it is a PDF file or else i was getting system files causing errors
        if '.pdf' in file:
            try:
                try_counter += 1
                finalname_list = []
                #extract OCR data and return to match with keywords:
                pypdf2_file = open_pdf(file)
                opened_file = pypdf2_file.getPage(0).extractText().lower()
                print(opened_file)
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
                        print(f'this is the file sent to autorename1 {file}')
                        auto_rename(pypdf2_file, file, finalname_list)
                    elif found_matchL2 is None:
                        ##If no L2 Keyword is found rename the file wihtout a L2keyword
                        #call file rename function
                        # I would like to add a function to add rules and rerun to get the second match
                        finalname_list.append([found_matchL1['type'], ' - ',
                        found_matchL1['prettyname'],
                        '.pdf'])
                        print(f'this is the file sent to autorename2 {file}')
                        auto_rename(pypdf2_file, file, finalname_list)
                #Catch files that dont match any rules
                else:
                    print(f'File did NOT match any rules {file}')
                    continue
            except:
                except_counter += 1
    # print(try_counter)
    # print(except_counter)
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