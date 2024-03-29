import os
import csv
import shutil

def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    if os.path.exists('analytics'):
        shutil.rmtree(r'analytics')
    os.mkdir('analytics')

def inValidRollNo(rollNo):
    if len(rollNo)!=8:
        return True
    if rollNo[0]<'0' and rollNo[0]>'9':
        return True
    if rollNo[1]<'0' and rollNo[1]>'9':
        return True
    if rollNo[2]<'0' or rollNo[2]>'2':
        return True
    if rollNo[3]<'1' or rollNo[3]>'2' or (rollNo[2]=='2' and rollNo[3]=='2'):
        return True
    branch={'CS','cs','EE','ee','ME','me','CB','cb','CE','ce','MT','mt','PH','ph','MA','ma','HS','hs','MA','ma','CH','ch','NT','nt'}
    x = rollNo[4:6]
    if x not in branch:
        return True
    if rollNo[6]<'0' and rollNo[6]>'9':
        return True
    if rollNo[7]<'0' and rollNo[7]>'9':
        return True
    return False


def course():
    # Read csv and process
    path = os.getcwd()
    os.mkdir(path+'\\analytics\\course')
    fieldNames = ['id','full_name','country','email','gender','dob','blood_group','state']
    degrees = {'01':'btech','11':'mtech','12':'msc','21':'phd'}
    with open('studentinfo_cs384.csv','r') as myFile:
        freader = csv.DictReader(myFile)
        for x in freader:
            if inValidRollNo(x['id']):
                if not os.path.exists(path+'\\analytics\\'+'course\\'+'misc.csv'):
                    with open(path+'\\analytics\\'+'course\\'+'misc.csv','a',newline='') as toEditFile:
                        fwriter = csv.DictWriter(toEditFile,fieldNames)
                        fwriter.writeheader()
                        fwriter.writerow(dict(x))
                else:
                    with open(path+'\\analytics\\'+'course\\'+'misc.csv','a',newline='') as toEditFile:
                        fwriter = csv.DictWriter(toEditFile,fieldNames)
                        fwriter.writerow(dict(x))
            else:
                joiningYear = x['id'][0:2]
                degreeCode = x['id'][2:4]
                spcl = x['id'][4:6]
                if not os.path.exists(path+'\\analytics\\course\\'+spcl.lower()+'\\'+degrees[degreeCode]):
                    os.makedirs(path+'\\analytics\\course\\'+spcl.lower()+'\\'+degrees[degreeCode])
                if not os.path.exists(path+'\\analytics\\course\\'+spcl.lower()+'\\'+degrees[degreeCode]+'\\'+joiningYear+'_'+spcl+'_'+degrees[degreeCode]+'.csv'):
                    with open(path+'\\analytics\\course\\'+spcl.lower()+'\\'+degrees[degreeCode]+'\\'+joiningYear+'_'+spcl+'_'+degrees[degreeCode]+'.csv','a',newline='') as toEditFile:
                        fwriter = csv.DictWriter(toEditFile, fieldNames)
                        fwriter.writeheader()
                        fwriter.writerow(dict(x))
                else:
                    with open(path+'\\analytics\\course\\'+spcl.lower()+'\\'+degrees[degreeCode]+'\\'+joiningYear+'_'+spcl+'_'+degrees[degreeCode]+'.csv','a',newline='') as toEditFile:
                        fwriter = csv.DictWriter(toEditFile, fieldNames)
                        fwriter.writerow(dict(x))

def country():
    # Read csv and process
    countryNames = set()
    path = os.getcwd()
    os.mkdir(path+'\\analytics\\country')
    fieldNames = ['id','full_name','country','email','gender','dob','blood_group','state']
    with open('studentinfo_cs384.csv','r') as myFile:
        freader=csv.DictReader(myFile)
        for x in freader:
            if x['country'] not in countryNames:
                countryNames.add(x['country'])
                with open(path+'\\analytics\\country\\'+x['country'].lower()+'.csv','w',newline='') as toEditFile:
                    fwriter = csv.writer(toEditFile)
                    fwriter.writerow(fieldNames)
    with open('studentinfo_cs384.csv','r') as myFile:
        freader=csv.DictReader(myFile)
        for x in freader:
            with open(path+'\\analytics\\country\\'+x['country'].lower()+'.csv','a',newline='') as toEditFile:
                fwriter = csv.DictWriter(toEditFile,fieldNames)
                fwriter.writerow(dict(x))


def email_domain_extract():
    # Read csv and process
    path = os.getcwd()
    os.mkdir(path + '\\analytics\\email_domain')
    fieldNames = ['id','full_name','country','email','gender','dob','blood_group','state']
    with open('studentinfo_cs384.csv','r') as myFile:
        freader=csv.DictReader(myFile)
        domainSet = set()
        for x in freader:
            domain=x['email']
            pos1=0
            pos2=0
            for i in range(len(domain)):
                if domain[i]=='@':
                    pos1=i+1
                    pos2=i+1
                    while domain[pos2] != '.':
                        pos2+=1
                    break
            domain = domain[pos1:pos2]
            with open(path+'\\analytics\\email_domain\\'+domain+'.csv','a',newline='') as toEditFile:
                fwriter = csv.DictWriter(toEditFile,fieldNames)
                if domain not in domainSet:
                    domainSet.add(domain)
                    fwriter.writeheader()
                fwriter.writerow(dict(x))


def gender():
    # Read csv and process
    path = os.getcwd()
    os.mkdir(path+'\\analytics'+'\\gender')
    fieldNames = ['id','full_name','country','email','gender','dob','blood_group','state']
    with open('studentinfo_cs384.csv','r') as myFile:
        freader = csv.DictReader(myFile)
        genders = set()
        for x in freader:
            with open(path+'\\analytics\\gender\\'+x['gender'].lower() +'.csv', 'a', newline='') as toEditFile:
                fwriter = csv.DictWriter(toEditFile,fieldNames)
                if x['gender'].lower() not in genders:
                    genders.add(x['gender'].lower())
                    fwriter.writeheader()
                fwriter.writerow(dict(x))


def dob():
    # Read csv and process
    path = os.getcwd()
    os.mkdir(path+'\\analytics\\'+'dob')
    fieldNames = ['id','full_name','country','email','gender','dob','blood_group','state']
    with open('studentinfo_cs384.csv') as myFile:
        freader = csv.DictReader(myFile)
        dateSet = set()
        for x in freader:
            date = x['dob']
            year = (int)(date[6:10])
            if year>=1995 and year<=1999:
                with open(path+'\\analytics\\dob\\'+'bday_1995_1999'+'.csv','a',newline='') as toEditFile:
                    fwriter = csv.DictWriter(toEditFile, fieldNames)
                    if 'bday_1995_1999' not in dateSet:
                        dateSet.add('bday_1995_1999')
                        fwriter.writeheader()
                    fwriter.writerow(dict(x))
            elif year<=2004:
                with open(path+'\\analytics\\dob\\'+'bday_2000_2004'+'.csv','a',newline='') as toEditFile:
                    fwriter = csv.DictWriter(toEditFile, fieldNames)
                    if 'bday_2000_2004' not in dateSet:
                        dateSet.add('bday_2000_2004')
                        fwriter.writeheader()
                    fwriter.writerow(dict(x))
            elif year<=2009:
                with open(path+'\\analytics\\dob\\'+'bday_2005_2009'+'.csv','a',newline='') as toEditFile:
                    fwriter = csv.DictWriter(toEditFile, fieldNames)
                    if 'bday_2005_2009' not in dateSet:
                        dateSet.add('bday_2005_2009')
                        fwriter.writeheader()
                    fwriter.writerow(dict(x))
            elif year<=2014:
                with open(path+'\\analytics\\dob\\'+'bday_2010_2014'+'.csv','a',newline='') as toEditFile:
                    fwriter = csv.DictWriter(toEditFile, fieldNames)
                    if 'bday_2010_2014' not in dateSet:
                        dateSet.add('bday_2010_2014')
                        fwriter.writeheader()
                    fwriter.writerow(dict(x))
            elif year<=2020:
                with open(path+'\\analytics\\dob\\'+'bday_2015_2020'+'.csv','a',newline='') as toEditFile:
                    fwriter = csv.DictWriter(toEditFile, fieldNames)
                    if 'bday_2015_2020' not in dateSet:
                        dateSet.add('bday_2015_2020')
                        fwriter.writeheader()
                    fwriter.writerow(dict(x))


def state():
    # Read csv and process
    path = os.getcwd()
    os.mkdir(path+'\\analytics\\state')
    fieldNames = ['id','full_name','country','email','gender','dob','blood_group','state']
    with open('studentinfo_cs384.csv','r') as myFile:
        freader = csv.DictReader(myFile)
        for x in freader:
            if not os.path.exists(path+'\\analytics'+'\\state\\'+x['state'].lower()+'.csv'):
                 with open(path+'\\analytics'+'\\state\\'+x['state'].lower()+'.csv', 'a',newline='') as toEditFile:
                     fwriter = csv.DictWriter(toEditFile,fieldNames)
                     fwriter.writeheader()
                     fwriter.writerow(dict(x))
            else:
                with open(path+'\\analytics'+'\\state\\'+x['state'].lower()+'.csv', 'a',newline='') as toEditFile:
                    fwriter = csv.DictWriter(toEditFile,fieldNames)
                    fwriter.writerow(dict(x))


def blood_group():
    # Read csv and process
    path = os.getcwd()
    os.mkdir(path+'\\analytics\\blood_group')
    fieldNames = ['id','full_name','country','email','gender','dob','blood_group','state']
    with open('studentinfo_cs384.csv','r') as myFile:
        freader = csv.DictReader(myFile)
        for x in freader:
            if not os.path.exists(path+'\\analytics'+'\\blood_group\\'+x['blood_group'].lower()+'.csv'):
                with open(path+'\\analytics'+'\\blood_group\\'+x['blood_group'].lower()+'.csv', 'a',newline='') as toEditFile:
                    fwriter = csv.DictWriter(toEditFile,fieldNames)
                    fwriter.writeheader()
                    fwriter.writerow(dict(x))
            else:
                with open(path+'\\analytics'+'\\blood_group\\'+x['blood_group'].lower()+'.csv', 'a',newline='') as toEditFile:
                    fwriter = csv.DictWriter(toEditFile,fieldNames)
                    fwriter.writerow(dict(x))


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    path = os.getcwd()
    fieldNames = ['id','first_name','last_name','country','email','gender','dob','blood_group','state']
    studentList = []
    with open('studentinfo_cs384.csv','r') as myFile:
        freader = csv.DictReader(myFile)
        for x in freader:
            name = x['full_name']
            nameSep = name.split(" ")
            firstName = nameSep[0]
            lastName = nameSep[1]
            if not os.path.exists('studentinfo_cs384_names_split.csv'):
                with open('studentinfo_cs384_names_split.csv','a',newline='') as toEditFile:
                    fwriter = csv.writer(toEditFile)
                    fwriter.writerow(fieldNames)
            else:
                with open('studentinfo_cs384_names_split.csv','a',newline='') as toEditFile:
                    fwriter = csv.writer(toEditFile)
                    tempList = [x['id'],firstName,lastName,x['country'],x['email'],x['gender'],x['dob'],x['blood_group'],x['state']]
                    fwriter.writerow(tempList)
            studentList.append([firstName,lastName,x['id'],x['country'],x['email'],x['gender'],x['dob'],x['blood_group'],x['state']])
    studentList.sort()
    with open('studentinfo_cs384_names_split_sorted_first_name.csv','a',newline='') as toEditFile:
        fwriter = csv.writer(toEditFile)
        fwriter.writerow(fieldNames)
        for x in studentList:
            fwriter.writerow([x[2],x[0],x[1],x[3],x[4],x[5],x[6],x[7],x[8]])
