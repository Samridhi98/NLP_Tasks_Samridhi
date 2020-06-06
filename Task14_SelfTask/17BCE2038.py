# -*- coding: utf-8 -*-
"""
Created on Fri May  8 01:44:16 2020

@author: Samridhi
"""
#importing libraries of general usage
import nltk
import re
#importing libraries for pdf extraction
# Base library: pdfminer
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox
#importing libraries for text pre-processing
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from collections import defaultdict



"""This function extracts text from PDFs present in a folder, named 'PDFs'.
Extracts text per paragraph"""
def pdf_to_text(path):
    text=[]
    resrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(resrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(resrcmgr, device)
    
    fp = open(path+".pdf", 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        layout = device.get_result()
        temp = []
        for ele in layout:
            #extracting text paragraph wise
            if isinstance(ele, LTTextBox):
                t = ele.get_text()
                if not t.isspace() and not len(t)==0:
                    temp.append(t)
        text.append(temp)
    fp.close()
    device.close()
    return text #returns overall extracted text

"""Preprocesses the text splitted into paragraphs. splitting each paragraph into tokens using tokeniser and 
removing stopwords as well as reducing words to their base forms."""
def preprocess_pdf(doc):
    global sent
    pattern = re.compile('\n+')
    sent_tokenizer = PunktSentenceTokenizer()
    texts = ''
    for j in doc:
        for i in j:
            raw = pattern.sub(' ',i)
            raw = sent_tokenizer.tokenize(raw)
            t=[]
            for k in raw:
                if k[-1]=='.':
                    t.append(k+" ")
            temp = ''.join(t)
            if len(temp)!=0:
                texts+=temp
    return texts
    

        
"""Pre_processing extracted data"""
def pre_process(doc):
    lemmatizer = WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words('english')
    text=nltk.sent_tokenize(doc)
    tokens = [[word for word in nltk.word_tokenize(sent)] for sent in text ]
    tokens= [[w for w in sent if w not in stopwords] for sent in tokens]
    tokens = [[w.lower() for w in sent if w.isalpha()] for sent in tokens ]
    #stems = [[stemmer.stem(t) for t in sent] for sent in tokens]
    lemma = [[lemmatizer.lemmatize(t) for t in sent] for sent in tokens]
    return lemma


"""Main function"""
if __name__ == "__main__":
    
    #Type of input
    print("\nTypes of input:\n1. Press 1 for 'Text File'\n2. Press 2 for 'PDF'", end=" ")
    my_type=int(input("Enter the type of input: "))
    
    #Extracting data from given file based on type
    doc = pdf_to_text(input("Enter the path of the file: "))   
    print ('Reading files...')
    data = preprocess_pdf(doc)
    docs=data
    
    #preprocessing files
    print ("Preprocessing data extracted...")
    documents=nltk.sent_tokenize(docs)
    texts=pre_process(docs)
    
    #remove words that appear only once
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    # texts = [[token for token in text if frequency[token] > 2] for text in texts]
            


