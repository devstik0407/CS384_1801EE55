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
    pass


def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
