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
    # rename Logic 
    

def rename_Sherlock(folder_name):
    # rename Logic 
    

def rename_Suits(folder_name):
    # rename Logic 
    

def rename_How_I_Met_Your_Mother(folder_name):
    # rename Logic 
    