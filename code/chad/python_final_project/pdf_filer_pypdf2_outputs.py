#Need to Install PyPDF2 reports supported version as py3.5 but runs fine in 3.6
import PyPDF2

f = open('/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/republicbill.pdf', 'rb')

pdfread = PyPDF2.PdfFileReader(f)

#{'/Parent': IndirectObject(2, 0), '/Contents': IndirectObject(13, 0), 
# '/PieceInfo': {'/PSL': {'/Private': {'/V': '3.2.9'}, '/LastModified': 
# "D:20151203211610-00'00'"}}, '/MediaBox': [0, 0, 606.24, 784.44], '/Resources': 
# {'/XObject': {'/Im0': IndirectObject(5, 0)}, '/Font': {'/T1_0': IndirectObject(11, 0)}, '/ProcSet': ['/PDF', 
# '/Text', '/ImageC']}, '/Type': '/Page', '/LastModified': "D:20151203141610-07'00'"}
#print(pdfread.getPage(0))

# {'/Parent': IndirectObject(2, 0), '/Contents': IndirectObject(13, 0), '/PieceInfo': {'/PSL': 
# {'/Private': {'/V': '3.2.9'}, '/LastModified': "D:20151203211610-00'00'"}}, '/MediaBox': 
# [0, 0, 606.24, 784.44], '/Resources': {'/XObject': {'/Im0': IndirectObject(5, 0)}, '/Font': 
# {'/T1_0': IndirectObject(11, 0)}, '/ProcSet': ['/PDF', '/Text', '/ImageC']}, '/Type': '/Page', 
# '/LastModified': "D:20151203141610-07'00'"}{'/CreationDate': "D:20151203141607-07'00'", 
# '/Creator': 'PFU ScanSnap Manager 6.3.27 #iX500 (W)', '/Producer': 'Adobe PDF Scan Library 3.2', 
# '/ModDate': "D:20151203141610-07'00'"}
#print(pdfread.getDocumentInfo())

#Didnt Get a Output
#print(pdfread.getFormTextFields(0))

# Didnt get an output
# print(pdfread.getObject())

#'}, '/LastModified': "D:20151203211610-00'00'"}}, '/MediaBox': [0, 0, 606.24, 784.44], '/Resources': {'/XObject': 
# {'/Im0': IndirectObject(5, 0)}, '/Font': {'/T1_0': IndirectObject(11, 0)}, '/ProcSet': ['/PDF', '/Text', '/ImageC']}, '/Type': '/Page', '/LastModified': "D:20151203141610-07'00'"}
#{'/CreationDate': "D:20151203141607-07'00'", '/Creator': 'PFU ScanSnap Manager 6.3.27 #iX500 (W)', '/Producer': 'AdobePDF Scan Library 3.2', '/ModDate': "D:20151203141610-07'00'"}
#Traceback (most recent call last):
pageobj = pdfread.getPage(0)
print(pageobj.extractText())

# print(pdfread.getXmpMetadata)
