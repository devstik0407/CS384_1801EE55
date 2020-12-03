import csv
import os
import re
import shutil
os.system('cls')
gradeToInteger = {
    "AA":10,
    "AB":9,
    "BB":8,
    "BC":7,
    "CC":6,
    "CD":5,
    "DD":4,
    "F":0,
    "I":0}
rollNumbers = set()
if os.path.exists(os.getcwd() + '\\'+'grades'): 
    shutil.rmtree(os.getcwd() + '\\'+'grades')
os.mkdir('grades')

def isValidRollNo(rollNo):
    #To check if a roll number is in proper format
    if len(rollNo)!=8:
        return False
    if rollNo[0]<'0' or rollNo[0]>'9':
        return False
    if rollNo[1]<'0' or rollNo[1]>'9':
        return False
    if rollNo[2]<'0' or rollNo[2]>'2':
        return False
    if rollNo[3]<'1' or rollNo[3]>'2' or (rollNo[2]=='2' and rollNo[3]=='2'):
        return False
    branch={'CS','cs','EE','ee','ME','me','CB','cb','CE','ce','MC','mc','MT','mt','PH','ph','MA','ma','HS','hs','MA','ma','CH','ch','NT','nt'}
    x = rollNo[4:6]
    if x not in branch:
        return False
    if rollNo[6]<'0' or rollNo[6]>'9':
        return False
    if rollNo[7]<'0' or rollNo[7]>'9':
        return False
    return True

def isValidGrade(grade):
    #To check if the given grade is valid
    if grade in gradeToInteger:
        return True
    return False

def isValidYear(year):
    #To check if the given year is valid
    if int(year)>2020:
        return False
    return True

def isValidSem(sem):
    #To check if the given sem is valid
    if int(sem)<1 or int(sem)>8:
        return False
    return True

def isValidSubject(subject):
    #To check if the given subject exists
    if len(subject)!=5:
        return False
    branch={'CS','cs','EE','ee','ME','me','CB','cb','CE','ce','MT','mt','MC','mc','SE','se','PH','ph','MA','ma','HS','hs','MA','ma','CH','ch','NT','nt'}
    if subject[0:2] in branch:
        pattern = re.compile("[0-9]{3}")
        if re.fullmatch(pattern,subject[2:5]):
            return True
        return False
    return False

def isValidEntry(entry):
    #To check if the entire row is correct
    if isValidRollNo(entry['roll']) and isValidGrade(entry['credit_obtained']) and isValidSem(entry['sem']) and isValidYear(entry['year']) and isValidSubject(entry['sub_code']):
        return True
    return False

def errorSeparation():
    #Stores the erroneous entries into misc.csv file
    path = os.getcwd()
    fileToRead = open(path+'\\acad_res_stud_grades.csv','r')
    csvReader = csv.DictReader(fileToRead)
    fileToWrite = open(path+"\\grades\\misc.csv","a",newline='')
    fieldname = ["sl","roll","sem","year","sub_code","total_credits","credit_obtained","timestamp","sub_type"]
    fwriter = csv.DictWriter(fileToWrite,fieldname)
    fwriter.writeheader()
    for row in csvReader:
        if not isValidEntry(row):
            fwriter.writerow(dict(row))

def makeRollNumberIndividual():
    #Creates rollnumber_individual.csv file 
    #corresponding to correct entries for a particular roll number
    path = os.getcwd()
    fileToRead = open(path+'\\acad_res_stud_grades.csv','r')
    fReader = csv.DictReader(fileToRead)
    fieldnames = ["Subject","Credits","Type","Grade","Sem"]
    cnt=0
    for row in fReader:
        if not isValidEntry(row):
            continue
        rollNumber = row['roll']
        fileToWrite = open(path+'\\grades\\'+rollNumber+'_individual.csv','a',newline='')
        fwriter = csv.DictWriter(fileToWrite,fieldnames)
        if rollNumber not in rollNumbers:
            fwriter.writeheader()
            rollNumbers.add(rollNumber)
            cnt+=1
        fwriter.writerow({'Subject':row['sub_code'],
                          'Credits':row['total_credits'],
                          'Type':row['sub_type'],
                          'Grade':row['credit_obtained'],
                          'Sem':row['sem']})

def makeRollNumberOverall():
    #Creates rollnumber_overall.csv file 
    #corresponding to correct entries for a particular roll number
    path = os.getcwd()
    cnt=0
    for roll in rollNumbers:
        cnt+=1
        fileToRead = open(path+'\\grades\\'+roll+'_individual.csv','r')
        freader = csv.DictReader(fileToRead)
        fieldname = ["Semester","Semester Credits","Semester Credits Cleared","SPI","Total Credits","Total Credits Cleared","CPI"]
        fileToWrite = open(path+'\\grades\\'+roll+'_overall.csv','a',newline='')
        fwriter = csv.DictWriter(fileToWrite, fieldname)
        fwriter.writeheader()
        credit = [0,0,0,0,0,0,0,0]
        spi = [0,0,0,0,0,0,0,0]
        for row in freader:
            sem = int(row['Sem'])-1
            credit[sem]+=int(row['Credits'])
            spi[sem]+=int(row['Credits'])*gradeToInteger[row['Grade']]
        totalCredit=0
        cpi=[0,0,0,0,0,0,0,0]
        for i in range(8):
            if credit[i]==0:
                continue
            spi[i]/=credit[i]
            totalCredit+=credit[i]
            if i==0:
                cpi[i]=spi[i]
            else:
                cpi[i]=(cpi[i-1]*(totalCredit-credit[i])+spi[i]*credit[i])/totalCredit
            fwriter.writerow({"Semester":i+1,
                             "Semester Credits":credit[i],
                             "Semester Credits Cleared":credit[i],
                             "SPI":round(spi[i],2),
                             "Total Credits":totalCredit,
                             "Total Credits Cleared":totalCredit,
                             "CPI":round(cpi[i],2)})

errorSeparation()          #To generate the misc.csv file containing erroneous entries    
makeRollNumberIndividual() #To generate the rollnumber_individual.csv files for correct entries
makeRollNumberOverall()    #To generate the rollnumber_overall.csv files for correct entries