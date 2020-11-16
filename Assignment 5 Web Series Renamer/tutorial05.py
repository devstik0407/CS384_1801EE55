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


webSeriesName = int(input("Enter main title of web series:"+
                          "\n1.FIR"+
                          "\n2.Game of Thrones"+
                          "\n3.How I Met Your Mother"+
                          "\n4.Sherlock"+
                          "\n5.Suits"+
                          "\nEnter a number corresponding to a particular web series:"))
seasonNumPadding = int(input("Enter season number padding - "))
episodeNumPadding = int(input("Enter episode number padding - "))
webSeries = ['FIR',
             'Game of Thrones',
             'How I Met Your Mother',
             'Sherlock',
             'Suits']
if webSeriesName == 1:
	rename_FIR(webSeries[0])
elif webSeriesName == 2:
	rename_Game_of_Thrones(webSeries[1])
elif webSeriesName == 3:
	rename_How_I_Met_Your_Mother(webSeries[2])
elif webSeriesName == 4:
	rename_Sherlock(webSeries[3])
elif webSeriesName == 5:
	rename_Suits(webSeries[4])