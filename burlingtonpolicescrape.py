import PyPDF2
import os.path

pdfFileObj = open(os.path.join(os.path.dirname(__file__), '2.pdf'), "rb")#open("/Users/Shared/2.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageContent = open("pdf output.txt", "w")
finalOutput = open("Final Output.txt", "w")
num_pages = pdfReader.numPages
count = 0
text = ""
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
if text != "":
   text = text

text = text.replace(',', '') #removes all commas
text = text.replace('20-',', 20-') #adds commas in front of each report number

pageContent.write(text) #writes string to text file

crashes = str(text.count("MV CRASH")) #counts crashes in text
stops = str(text.count("MV STOP")) # stops in text
tickets = str(text.count("Citation/Warning Issued")) # warnings in text
ambulance = str(text.count("Ambulance Request")) #ambulance requests in string
hangups = str(text.count("911 Aband/ Hang Up Logged")) # 911 hangups in string
roadHazard = str(text.count("ROAD HAZARD")) # road hazards in string
susperson = str(text.count("SUSP PERSON")) # suspicious persons in text

output = (crashes+' Motor Vehicle Accidents, '
    +stops+' Motor Vehicle Stops, '
    +tickets+' Citation/Warnings Issued, '
    +ambulance+' Ambulance Requests, '
    +hangups+' 911 Hangups, '
    +roadHazard+' road hazard calls, '
    +susperson+' suspicious persons calls')

finalOutput.write(output)

print("")
print("")
print("")
print('There have been: ') #prints all the results
print(crashes+' Motor Vehicle Accidents ')
print(stops+' Motor Vehicle Stops')
print(tickets+' Citation/Warnings Issued')
print(ambulance+' Ambulance Requests')
print(hangups+' 911 Hangups')
print(roadHazard+' road hazard calls')
print(susperson+' suspicious persons calls')