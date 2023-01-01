import fitz
import os
import re

corpus=[]
doc=""
folder= os.listdir('pdffiles')
for file in folder:
    with fitz.open(rf"pdffiles/{file}") as pdf:
        for page in pdf:
            text=page.get_text()
            doc=doc+text
        corpus.append(doc)
    print("file added to corpus")


text= corpus[0][-100:]

def preprocess(text):
    text= re.sub(r'[^\w\s\']',' ',text)
    text= re.sub(r'[ \n]+',' ',text)
    text = re.sub('[^a-zA-Z ]')
    return text.strip().lower()

preprocess(text)