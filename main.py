import pyttsx3
import PyPDF2
book = open("python3_tutorial.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
sp = speaker.getProperty('rate')
volume=speaker.getProperty('volume')
speaker.setProperty('volume', volume-4.00)
speaker.setProperty('rate', 110)
age=speaker.getProperty('age')
speaker.setProperty('age', 18)
speaker.setProperty('gender', 'male')
print(sp)
page = pdfReader.getPage(262)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()