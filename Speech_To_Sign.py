import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
import sys
import argparse
from nltk.parse.stanford import StanfordParser
from nltk.tag.stanford import StanfordPOSTagger, StanfordNERTagger
from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tree import *
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import nltk
import speech_recognition as sr
import time
#import selecting
# obtain audio from the microphone
def speak():
        
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            start_time = time.time()
            while True:
                try:
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, timeout=5)
                    if audio:
                        text = recognizer.recognize_google(audio)
                        print("You said:", text)
                        if any(exit_phrase in text.lower() for exit_phrase in ["goodbye", "good bye", "bye"]):
                                print("Exiting...")
                                sys.exit()
                        return text
                    else:
                        print("No speech detected for 5 seconds. Exiting...")
                        
                        # Check if 10 seconds have passed
                    if time.time() - start_time >= 10:
                        print("Exiting after 10 seconds.")
                        break
                except sr.UnknownValueError:
                    print("Could not understand audio.")
                    
                except sr.WaitTimeoutError:
                    print("No speech detected for 5 seconds. Exiting...")
                    break

                except KeyboardInterrupt:
                    break

        print("Program has stopped executing.")

def func():
        r = speak()
        inputString = " "
        import os
        java_path = "C:\\Program Files\\Java\\jdk-9.0.4\\bin\\java.exe"
        os.environ['JAVAHOME'] = java_path
        for each in range(1,len(sys.argv)):
            inputString += sys.argv[each]
            inputString += " "
        from nltk.parse.corenlp import CoreNLPParser
        inputString = r
        parser = CoreNLPParser(url='http://localhost:9001')
        englishtree=[tree for tree in parser.parse(inputString.split())]
        parsetree=englishtree[0]
        dict={}
        parenttree= ParentedTree.convert(parsetree)
        for sub in parenttree.subtrees():
            dict[sub.treeposition()]=0
        #"----------------------------------------------"
        isltree=Tree('ROOT',[])
        i=0
        for sub in parenttree.subtrees():
            if(sub.label()=="NP" and dict[sub.treeposition()]==0 and dict[sub.parent().treeposition()]==0):
                dict[sub.treeposition()]=1
                isltree.insert(i,sub)
                i=i+1
            if(sub.label()=="VP" or sub.label()=="PRP"):
                for sub2 in sub.subtrees():
                    if((sub2.label()=="NP" or sub2.label()=='PRP')and dict[sub2.treeposition()]==0 and dict[sub2.parent().treeposition()]==0):
                        dict[sub2.treeposition()]=1
                        isltree.insert(i,sub2)
                        i=i+1
        for sub in parenttree.subtrees():
            for sub2 in sub.subtrees():
        #         print(sub2)
        #         print(len(sub2.leaves()))
        #         print(dict[sub2.treeposition()])
                if(len(sub2.leaves())==1 and dict[sub2.treeposition()]==0 and dict[sub2.parent().treeposition()]==0):
                    dict[sub2.treeposition()]=1
                    isltree.insert(i,sub2)
                    i=i+1
        parsed_sent=isltree.leaves()
        words=parsed_sent
        stop_words=set(stopwords.words("english"))
        # print stop_words
        lemmatizer = WordNetLemmatizer()
        ps = PorterStemmer()
        lemmatized_words=[]
        for w in parsed_sent:
            # w = ps.stem(w)
            lemmatized_words.append(lemmatizer.lemmatize(w))

        islsentence = ""
        print('After NLP for ISL grammar')
        print(lemmatized_words)
        for w in lemmatized_words:
            if w not in stop_words:
                islsentence+=w
                islsentence+=" "
        print(islsentence)
        
        isl_gif=['thank you','any questions', 'are you angry', 'are you busy', 'are you hungry', 'be careful','did you finish homework',  'do you have money',
                'do you want something to drink', 'do you watch TV', 'dont worry', 'flower is beautiful',
                'good afternoon', 'good morning', 'good question', 'had your lunch', 'happy journey',
                'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing', 
                 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i go to a theatre', 'i love to shop',
                'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
                'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
                'please clean the room', 'please give me your pen', 'please wait for sometime', 'shall i help you',
                'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
                'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
                'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go',
                'where is the bathroom', 'where is the police station', 'you are wrong','address','agra','ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
'bihar','bihar','bridge','cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile','dasara',
'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
'voice', 'wednesday', 'weight','please wait for sometime','what is your mobile number','what are you doing','are you busy']
        
        
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']
        with sr.Microphone() as source:
                # image   = "signlang.png"
                # msg="HEARING IMPAIRMENT ASSISTANT"
                # choices = ["Live Voice","All Done!"] 
                # reply   = buttonbox(msg,image=image,choices=choices)
                #r.adjust_for_ambient_noise(source) 
                i= 0
                n = 1
                while n:
                        print("I am Listening")
                        #audio = r.listen(source)
                        # recognize speech using Sphinx
                        try:
                                #a=r.recognize_google(audio)
                                a = r
                                a = a.lower()
                                #print('You Said: ' + a.lower())
                                
                                for c in string.punctuation:
                                    a= a.replace(c,"")
                                    
                                if(a.lower()=='goodbye' or a.lower()=='good bye' or a.lower()=='bye'):
                                        print("oops!Time To say good bye")
                                        break
                                
                                elif(a.lower() in isl_gif):
                                    
                                    class ImageLabel(tk.Label):
                                            """a label that displays images, and plays them if they are gifs"""
                                            def load(self, im):
                                                if isinstance(im, str):
                                                    im = Image.open(im)
                                                self.loc = 0
                                                self.frames = []

                                                try:
                                                    for i in count(1):
                                                        self.frames.append(ImageTk.PhotoImage(im.copy()))
                                                        im.seek(i)
                                                except EOFError:
                                                    pass

                                                try:
                                                    self.delay = im.info['duration']
                                                except:
                                                    self.delay = 100

                                                if len(self.frames) == 1:
                                                    self.config(image=self.frames[0])
                                                else:
                                                    self.next_frame()

                                            def unload(self):
                                                self.config(image=None)
                                                self.frames = None

                                            def next_frame(self):
                                                if self.frames:
                                                    self.loc += 1
                                                    self.loc %= len(self.frames)
                                                    self.config(image=self.frames[self.loc])
                                                    self.after(self.delay, self.next_frame)
                                    root = tk.Tk()
                                    lbl = ImageLabel(root)
                                    lbl.pack()
                                    lbl.load(r'ISL_Gifs/{0}.gif'.format(a.lower()))
                                    root.mainloop()
                                else:
                                    for i in range(len(a)):
                                                    if(a[i] in arr):
                                            
                                                            ImageAddress = 'letters/'+a[i]+'.jpg'
                                                            ImageItself = Image.open(ImageAddress)
                                                            ImageNumpyFormat = np.asarray(ImageItself)
                                                            plt.imshow(ImageNumpyFormat)
                                                            plt.draw()
                                                            plt.pause(0.8)
                                                    else:
                                                            continue

                        except:
                               print(" ")
                        plt.close()

                        n -= 1
                        
while 1:
  image   = "signlang.jpeg"
  msg="HEARING IMPAIRMENT ASSISTANT"
  choices = ["Live Voice","All Done!"] 
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()
