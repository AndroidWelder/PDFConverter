'''
Created on Oct 16, 2022

@author: New User
'''
import PyPDF2
from gtts import gTTS
import os
from googletrans import Translator


def convertToText(path):
    #method that converts PDF to Text format
    #open file, where 'rb' stands for 'read binary'
    pdf_file=open(path,'rb')
    #create reader variable to read pdfFile
    pdf_reader=PyPDF2.PdfFileReader(pdf_file)
    #create variable for number of pages
    pages=pdf_reader.numPages
    #for testing purposes, print number of pages
    print('No. of pages: ' + str(pages))
    #create while loop that will compile multiple PDF pages
    i=0
    while i <= pages-1:
        if i == 0:
            text = pdf_reader.getPage(i).extractText()
        else:
            text = text + pdf_reader.getPage(i).extractText()
        i+=1
    #close pdf_file object
    pdf_file.close()
    
    return text

def convertToAudio(path):
    #method to convert PDF to Audio format
    filename = "PDFToAudio.mp3"
    #convert PDF to text
    text = convertToText(path)
    #create Text-to-speech variable
    tts = gTTS(text)
    #save MP3 of text converted to audio
    tts.save(filename)
    #play MP3 file out loud
    os.system("start " + filename)
    
    return "Saved in: " + os.path.abspath(filename), text

def translate(path, language):
    #method to translate PDF
    text = convertToText(path)
    #define Translator
    translator = Translator()
    #create variable for translated text
    translated = translator.translate(text, src='en', dest=language)

    return translated.text

#------------------------------------------------------------------
#replace the body of convertToAudio(path) with the following code if you prefer to use a Text-to-speech client that is entirely offline.
#
#method converts PDF to Audio format using pyttsx3 rather than gTTS
#    filename = "PDFToAudio.mp3"
#    
#    engine = pyttsx3.init()
#
#    text = convertToText(path)
#
#    engine.say(text)
#
#    engine.save_to_file(text, filename)
#
#    engine.runAndWait()
#    
#    return "Saved in: " + os.path.abspath(filename), text
#
#------------------------------------------------------------------