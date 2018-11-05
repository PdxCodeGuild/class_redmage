#Need to Install PyPDF2 reports supported version as py3.5 but runs fine in 3.6
#http://pybrary.net/pyPdf/pythondoc-pyPdf.pdf.html
import PyPDF2

f = open('republicbill.pdf', 'rb')

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

#---------------------------
#o^REPUBLICsEftvices1501RodgersStMissoulaMT59802-1735AdivisionofREPUBLICSERVICESAccountSummary3-0889-0024742September28,20150889-001617659$372.59-$372.59$0.00$394.32AccountNumberInvoiceDateInvoiceNumberPreviousBalancePayments/AdjustmentsUnpaidBalanceCurrentInvoiceChargesPayThisAmount$394.32DueBy:10/18/15ContactInformationMissoulaCustomersFlathead/LakeCounty(406)543-3157(800)823-8231ImportantInformationEFFECTIVEDECEMBER1,2008.THEFRF%WILL
# BEADJUSTEDMONTHLYINACCORDANCEWITHMARKETPRICEFLUCTUATIONSFOROURMISSOULACOUNTYCOMMERCIALANDINDUSTRIALCUSTOMERS,THEREWILLBEARATEINCREASEEFFECTIVEOCTOBER1,2015.Manageyouraccountonline24/7,onanydevicewithMyResource.Visitrepubliconline.comtogetstarted.A^^REPUBLICSEmnces1501RodgersStMissoulaMT59802-1735HAPPYVALLEYTRLCOURTInvoiceManagingyouraccountIsnoweasierthanever
# withtheMyResourceApp.FreedownloadonPage1of2
# theAppStoreorGooglePlay.Payments/AdjustmentsDateDescription09/10Payment-ThankYouCurrentInvoiceChargesHappyValleyTrICourt1251TremperRd(LI)CSA072314Missoula,MT2-
# RearLoad(3Yd)ScheduledService(31)DateDescription08/28ExtraYardage09/28RateAdjustment10/01/15-10/31/1509/28BasicService10/01/15-10/31/15TotalFuel
# RecoveryFeeCurrentInvoiceChargesReferenceReferenceElectronicPmtAmount-$372,59QuantitvUnitPriceAmount1.0000$10.30$10,302,0000$374.40$10.90$363.50$363.50$9.62$394.32CURRENT30DAYS60DAYS90+DAYS394.320.000.000.00OAŁWithMyResourceyoucanscheduleapickup,payyourbillanddiscovernewservices-all
# withatouchofabutton.Visitrepubllconline.comtogetstarted.ŁPleaseseereversesidefortermsandconditions.PleaseReturnThisPortionWithPaymentTOTALENCLOSEDPayThisAmountAccountNurnberInvoiceDateInvoiceNumberPayment^ueDate$394.323-0889-0024742September28,2015
# J0889-001617659October18,2015ReturnServiceRequested0021731AV
# 0.391170138HAPPYVALLEYTRLCOURTAFFORDABLEHOMES1208GROVESTMISSOULAMT59804-1350^Ml'.!Coin[.iletoRovrr-,:;30flfl'=iDD5M7M5D0DDD01bl7bSTDD003'=m3EDaaD3TM3aEMakeChecksPayableTo:REPUBLICSERVICES#889PCBOX78829PHOENIXAZ85062-8829
# number_of_pages = pdfread.getNumPages()
# page = pdfread.getPage(0)
# page_content = page.extractText()
# print(page_content)
# -------------------
# n the case of our PDF document (sample.pdf), the returned value is none, which means that the page mode is not specified.
# If you want to specify a page mode, you can use the method setPageMode(mode), where mode is one of the modes listed in the table above.
# Page Mode
# The PDF page comes with different modes, which are as follows:
#
# /UseNone	Do not show outlines or thumbnails panels
# /UseOutlines
# Show outlines (aka bookmarks) panel
# /UseThumbs
# Show page thumbnails panel
# /FullScreen
# Fullscreen view
# /UseOC
# Show Optional Content Group (OCG) panel
# /UseAttachments
# Show attachments panel
#-----------------------
#None returned below shows no mode has been set and can be set from above
# page = pdfread.getPage(0)
# page_mode = pdfread.documentInfo
# print(page_mode)
# print(page_mode['/Producer']) #Adobe PDF Scan Library 3.2
# print(page_mode['/Creator'])    # PFU ScanSnap Manager 6.3.27 #iX500 (W)
# print(page_mode['/CreationDate']) #D:20151203141607-07'00'

page = pdfread.getPage(0)
page_mode = page.extractText()


page_mode = page_mode.lower()
print(page_mode)

if 'republice' in page_mode:
    print('found text')