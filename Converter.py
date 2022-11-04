'''
Created on Oct 13, 2022

@author: New User
'''

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
import Controller

#creates app window in Tkinter
window = Tk()
window.geometry("500x300")

#variable that indicates if a document is uploaded or not
uploaded = False

def open_file():
    #this function allows user to browse system and select a file
    global uploaded
    global file
    file = filedialog.askopenfile(mode='r', filetypes=[('PDF files', '*.pdf')])
    if file:
        print("You uploaded a PDF!")
        uploaded = True
        file.close()
        
def clearText():
    #This function clears textbox when "Clear" button clicked.
    T1.delete('1.0', 'end')
               

class Requests(Frame):    
    
    def convert(self):
        #this function executes the conversion requested when "Go!" is clicked.  
        #it selects which conversion to execute, and resets the request frame after each selection.
        if uploaded == False:
            message = "You must upload a file first."
            self.reset_request_frame()
        elif self.radiovar.get() == 1:
            print ("\'Convert to text\' selected.")
            message = Controller.convertToText(file.name)
            self.reset_request_frame()
        elif self.radiovar.get() == 2:
            print ("\'Convert to audio\' selected.")
            message = Controller.convertToAudio(file.name)
            self.reset_request_frame()
        elif self.dropdownvar.get() == '<Select a language>':
            print ("No conversion selected.")
            message = "Please select the desired conversion."
            self.reset_request_frame()
        elif self.dropdownvar != '<Select a language>':
            if self.dropdownvar.get() not in self.langfull:
                print("Language not selected.")
                message = "Please select a language from the drop-down menu."
                self.reset_request_frame()
            else:
                print ("Translation into " + self.dropdownvar.get() + " selected.")
                langkey = self.langfull.index(self.dropdownvar.get())
                message = Controller.translate(file.name, self.langshort[langkey])
                self.reset_request_frame()
        else:
            message = "Please select the desired conversion."
            self.reset_request_frame()

        T1.insert(INSERT, message)
        
    def __init__(self, parent):
        #this method initializes the request frame
        Frame.__init__(self,parent)
        self.parent = parent
        self.parent.title("PDF translator and audio converter")

        request_frame = Frame(window, padx=10, pady=10, bg='#750412')
        request_frame.grid(row=0, column=0, sticky=N+S+E+W)

        #variables for radiobuttons and Combobox
        self.radiovar = IntVar()
        self.radiovar.set(0)
        self.dropdownvar = StringVar()
        self.dropdownvar.set('<Select a language>')

        #drop down menu language list, taken from print(googletrans.LANGUAGES), which yields all languages supported by Python
        self.langdictionary = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
        self.langfull = list(self.langdictionary.values())
        self.langshort = list(self.langdictionary.keys())

        #all widgets in request_frame
        self.B1 = Button(request_frame, relief='raised', text='Upload PDF', command=open_file, bg='#1273de', fg='#FFFFFF').grid(row=0, column=0)
        self.R1 = Radiobutton(request_frame, text='Convert to text', variable=self.radiovar, value=1, bg='#750412', fg='#000000').grid(row=1, column=0, sticky=W)
        self.R2 = Radiobutton(request_frame, text='Convert to audio', variable=self.radiovar, value=2, bg='#750412', fg='#000000').grid(row=2, column=0, sticky=W)
        self.L1 = Label(request_frame, text='Translate into...', bg='#750412', fg='#000000').grid(row=3, column=0, sticky=W)
        self.CB1 = ttk.Combobox(request_frame, textvariable=self.dropdownvar, values=[*self.langfull]).grid(row=6, column=0)
        self.CB1style = ttk.Style()
        self.CB1style.theme_use('clam')
        self.B2 = Button(request_frame, relief='raised', text='GO!', command=self.convert, bg='#1273de', fg='#FFFFFF').grid(row=7, column=0, pady=10, sticky=S)

    def reset_request_frame(self):
        #resets radiobuttons and combobox ever time "Go!" is clicked, so that user can make new selection.
        print("Service request frame reset.")
        self.radiovar.set(0)
        self.dropdownvar.set('<Select a language>')
     

#parent widget for output and clear output button
output_frame = Frame(window, padx=10, pady=10, bg='#c90d0d')
output_frame.grid(row=0, column=1, rowspan=4, sticky=N+S+E+W)

#all widgets in output_frame
T1 = scrolledtext.ScrolledText(output_frame, height=12, width=40)
T1.grid(row=0, column=0, sticky='n'+'s'+'e'+'w')
B3 = Button(output_frame, relief='raised', text='Clear', command=clearText, bg='#1273de', fg='#FFFFFF').grid(row=1, column=0, pady=10, sticky=S)

#enables output_frame to expand when window expands, while keeping request_frame the same size
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

output_frame.rowconfigure(0, weight=1)
output_frame.columnconfigure(0, weight=1)

#parent widget for service request widgets: upload button, radiobuttons, dropdown menu, go button.
request_frame = Requests(window)

mainloop()