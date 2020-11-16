import re
import os
seasonNumPadding = 3
episodeNumPadding = 3

def rename_FIR(folder_name):
    path = os.getcwd() + "\\Subtitles\\" + folder_name
    listOfFiles = os.listdir(path)
    for fileName in listOfFiles:
        try:
            text = re.findall('\d+',fileName)
            episodeNum = (text[0]).strip()
            extension = (re.split('\.',fileName)[-1]).strip()
            if len(episodeNum) < episodeNumPadding :
                episodeNum = '0'*(episodeNumPadding - len(episodeNum)) + episodeNum
            os.rename(path+'\\'+fileName,path+'\\'+'FIR - Episode '+ episodeNum + '.' + extension)
        except:
            os.remove(path+'\\'+fileName)

def rename_Game_of_Thrones(folder_name):
    path = os.getcwd() + "\\Subtitles\\" + folder_name
    listOfFiles = os.listdir(path)
    for fileName in listOfFiles:
        try:
            bagOfWords = re.split('-',fileName)
            seasonNum = (re.split('x',bagOfWords[1])[0]).strip()
            episodeNum = (re.split('x',bagOfWords[1])[1]).strip()
            extension = (re.split('\.',bagOfWords[-1])[-1]).strip()
            title = (re.split('\.',bagOfWords[2])[0]).strip()
            if len(episodeNum) < episodeNumPadding :
                episodeNum = '0'*(episodeNumPadding - len(episodeNum)) + episodeNum
            if len(seasonNum) < seasonNumPadding :
                seasonNum = '0'*(seasonNumPadding - len(seasonNum)) + seasonNum
            os.rename(path+'\\'+fileName,path+'\\'+'Game of Thrones - Season'+seasonNum+' Episode '+episodeNum+' - '+title+'.'+extension)
        except:
            os.remove(path+'\\'+fileName)

def rename_Sherlock(folder_name):
    path = os.getcwd() + "\\Subtitles\\" + folder_name
    listOfFiles = os.listdir(path)
    for fileName in listOfFiles:
        try:
            bagOfNumbers = re.findall('\d+',fileName)
            seasonNum = bagOfNumbers[0]
            episodeNum = bagOfNumbers[1]
            extension = (re.split('\.',fileName)[-1]).strip()
            if len(episodeNum) < episodeNumPadding :
                episodeNum = '0'*(episodeNumPadding - len(episodeNum)) + episodeNum
            if len(seasonNum) < seasonNumPadding :
                seasonNum = '0'*(seasonNumPadding - len(seasonNum)) + seasonNum
            os.rename(path+'\\'+fileName,path+'\\'+'Sherlock - Season'+seasonNum+' Episode '+episodeNum+'.'+extension)
        except:
            os.remove(path+'\\'+fileName)

def rename_Suits(folder_name):
    path = os.getcwd() + "\\Subtitles\\" + folder_name
    listOfFiles = os.listdir(path)
    for fileName in listOfFiles:
        try:
            bagOfWords = re.split('-',fileName)
            seasonNum = (re.split('x',bagOfWords[1])[0]).strip()
            episodeNum = (re.split('x',bagOfWords[1])[1]).strip()
            extension = (re.split('\.',bagOfWords[-1])[-1]).strip()
            title = (re.split('\.',bagOfWords[2])[0]).strip()
            if len(episodeNum) < episodeNumPadding :
                episodeNum = '0'*(episodeNumPadding - len(episodeNum)) + episodeNum
            if len(seasonNum) < seasonNumPadding :
                seasonNum = '0'*(seasonNumPadding - len(seasonNum)) + seasonNum
            os.rename(path+'\\'+fileName,path+'\\'+'Suits - Season'+seasonNum+' Episode '+episodeNum+' - '+title+'.'+extension)
        except:
            os.remove(path+'\\'+fileName)

def rename_How_I_Met_Your_Mother(folder_name):
    path = os.getcwd() + "\\Subtitles\\" + folder_name
    listOfFiles = os.listdir(path)
    for fileName in listOfFiles:
        try:
            bagOfWords = re.split('-',fileName)
            seasonNum = (re.split('x',bagOfWords[1])[0]).strip()
            episodeNum = (re.split('x',bagOfWords[1])[1]).strip()
            extension = (re.split('\.',bagOfWords[-1])[-1]).strip()
            title = (re.split('\.',bagOfWords[2])[0]).strip()
            if len(episodeNum) < episodeNumPadding :
                episodeNum = '0'*(episodeNumPadding - len(episodeNum)) + episodeNum
            if len(seasonNum) < seasonNumPadding :
                seasonNum = '0'*(seasonNumPadding - len(seasonNum)) + seasonNum
            os.rename(path+'\\'+fileName,path+'\\'+'How I Met Your Mother - Season'+seasonNum+' Episode '+episodeNum+' - '+title+'.'+extension)
        except:
            os.remove(path+'\\'+fileName)
