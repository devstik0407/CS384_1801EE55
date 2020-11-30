import os
import csv
import shutil
if os.path.exists(os.getcwd()+"\\"+"groups"):
    shutil.rmtree(os.getcwd()+"\\"+"groups")
os.mkdir("groups")
def group_allocation(filename, number_of_groups):
    path = os.getcwd()
    fileToRead = open(path+"\\"+filename,"r")
    freader = csv.DictReader(fileToRead)
    branch = {}
    student = []
    totalCount = 0
    for row in freader:
        roll =  row["Roll"]
        student.append([row["Roll"],row["Name"],row["Email"]])
        if roll[4:6].upper() in branch:
            branch[roll[4:6].upper()] += 1
        else:
            branch[roll[4:6].upper()] = 1
        totalCount+=1
    fileToRead.close()
    fileBranchStrength = open(path+"\\groups\\branch_strength.csv","a",newline='')
    fwriter = csv.DictWriter(fileBranchStrength, ["BRANCH_CODE","STRENGTH"])
    fwriter.writeheader()
    branchList = []
    for dept in branch:
        branchList.append([-branch[dept],dept])
    branchList = sorted(branchList)
    statsFieldname = ["group","total"]
    student = sorted(student)
    groupStats = []
    rem = {}
    for i in range(len(branchList)):
        fwriter.writerow({"BRANCH_CODE":branchList[i][1],"STRENGTH":(-branchList[i][0])})
        rem[branchList[i][1]] = (-branchList[i][0])%number_of_groups
        for grpNum in range(number_of_groups):
            if len(groupStats) <= grpNum:
                groupStats.append({})
            groupStats[grpNum][branchList[i][1]] = (-branchList[i][0])//number_of_groups
        statsFieldname.append(branchList[i][1])
    fileBranchStrength.close()
    prev = 0
    for dept in rem:
        cnt = rem[dept]
        while cnt>0:
            groupStats[prev][dept] += 1
            prev = (prev+1)%number_of_groups
            cnt -= 1
    branch = set()
    for i in range(len(student)):
        roll = student[i][0]
        fileToWrite = open(path+"\\groups\\"+roll[4:6].upper()+".csv","a",newline='')
        fieldname = ["Roll","Name","Email"]
        fwriter = csv.DictWriter(fileToWrite, fieldname)
        if roll[4:6].upper() not in branch:
            fwriter.writeheader()
            branch.add(roll[4:6].upper())
        fwriter.writerow({"Roll":student[i][0],"Name":student[i][1],"Email":student[i][2]})
    group_G = set()
    cnt = 0
    for i in range(len(branchList)):
        dept = branchList[i][1]
        fileToRead = open(path+"\\groups\\"+dept+".csv","r")
        freader = csv.DictReader(fileToRead)
        grpNum = -1
        x = 0
        for row in freader:
            if x == 0:
                grpNum += 1
                x = groupStats[grpNum][dept]
            grp = str(grpNum+1)
            if len(grp) < 2:
                grp = "0"*(2-len(grp))+grp
            grp = "Group_G"+grp
            fileToWrite = open(path+"\\groups\\"+grp+".csv","a",newline='')
            fwriter = csv.DictWriter(fileToWrite,["Roll","Name","Email"])
            if grp not in group_G:
                fwriter.writeheader()
                group_G.add(grp)
            fwriter.writerow(dict(row))
            x -= 1
        fileToRead.close()
    cnt = 0
    statsFile = open(path+"\\groups\\"+"stats_grouping.csv","a",newline='')
    statsWriter = csv.DictWriter(statsFile,statsFieldname)
    statsWriter.writeheader()
    for grpNum in range(number_of_groups):
        totalEntries = 0
        rowToAdd = {}
        for dept in groupStats[grpNum]:
            totalEntries += groupStats[grpNum][dept]
            rowToAdd[dept] = groupStats[grpNum][dept]
        grp = str(grpNum+1)
        if len(grp) < 2:
            grp = "0"*(2-len(grp))+grp
        grp = "Group_G"+grp
        rowToAdd["group"] = grp
        rowToAdd["total"] = totalEntries
        statsWriter.writerow(dict(rowToAdd))

filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)