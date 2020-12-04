import time 
import os
import sys
import csv
import re
import threading
import keyboard
import sqlite3 as sq3
from tkinter import *
from tkinter import messagebox
   
if not os.path.exists(os.getcwd()+"\\quiz_wise_responses"):
    os.mkdir("quiz_wise_responses")
if not os.path.exists(os.getcwd()+"\\individual_responses"):
    os.mkdir("individual_responses")
temp = 1000

def runTimer(hrs,mins,secs):
    
    root = Tk()
    root.geometry("200x100")

    root.title("Time Counter")
    
    hour=StringVar()
    minute=StringVar()
    second=StringVar()
    
    hour.set("00")
    minute.set("00")
    second.set("00")
    
    hourEntry= Entry(root, width=3, font=("Arial",10,"bold"),
                 textvariable=hour, bg = "#000000",fg = "white")
    hourEntry.place(x=45,y=35)
    
    minuteEntry= Entry(root, width=3, font=("Arial",10,"bold"),
                       textvariable=minute, bg = "#000000", fg = "white")
    minuteEntry.place(x=85,y=35)
  
    secondEntry= Entry(root, width=3, font=("Arial",10,"bold"),
                   textvariable=second, bg = "black", fg = "white")
    secondEntry.place(x=125,y=35)
    global temp
    try:
        temp = int(hrs)*3600 + int(mins)*60 + int(secs)
    except:
        print("Please input the right value")
    while temp >-1:
        hours = temp//3600
        mins = (temp%3600)//60
        secs = (temp%3600)%60
         
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        root.update()
        time.sleep(1)
            
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        temp -= 1
    root.mainloop()
    


registerFails = 0
loginFails = 0

maxRegisterFails = 8
maxLoginFails = 8

def register():
    global registerFails
    conn = sq3.connect("project1_quiz_cs384.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS project1_registration(
        Username TEXT PRIMARY KEY,
        Password TEXT,
        Name TEXT,
        Whatsapp Number TEXT);''')
    conn.commit()
    name = str(input("Enter your full name: "))
    username = str(input("Enter your roll number as username: "))
    password = str(input("Enter your password (at least 6 letters, 1 digit and 1 special character): "))
    whatsNum = str(input("Enter your whatsapp number: "))
    try:
        entry = (username,password,name,whatsNum)
        conn.execute("INSERT INTO project1_registration VALUES(?,?,?,?)",entry)
        conn.commit()
        registerFails = 0
        print("You have successfully registered\nNow you can log in")
        return login()
    except:
        print("::ERROR::\nPlease check your username and password")
        registerFails += 1
        if registerFails >= maxRegisterFails:
            print("Please try again later")
            return -1
        return register()

def login():
    global loginFails
    global username
    conn = sq3.connect("project1_quiz_cs384.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS project1_registration(
        Username TEXT PRIMARY KEY,
        Password TEXT,
        Name TEXT,
        Whatsapp Number TEXT);''')
    conn.commit()
    username = str(input("Enter your roll number as username: "))
    password = str(input("Enter your password (at least 6 letters, 1 digit and 1 special character): "))
    entry = conn.execute("SELECT Name FROM project1_registration WHERE Username = ? AND Password = ?",(username,password))
    if entry.fetchone() != None:
        loginFails = 0
        print("You have successfully logged in")
        conn.close()
        return 0
    else:
        print("::ERROR::\nPlease check your username and password")
        loginFails += 1
        conn.close()
        if loginFails >= maxLoginFails:
            print("Please try again later")
            return -1
        return login()


def conductQuiz(quizName,rollNumber):
    global question_list
    global unattempted_question
    global marked_choice
    global obtained_marks
    global total_marks
    global unattempted
    global correct_choices
    global wrong_choices
    global total_questions
    
    path = os.getcwd()
    qFile = open(path+"\\quiz_wise_questions\\q"+quizName[4:]+".csv","r")
    freader = csv.DictReader(qFile)
    
    marked_choice = []
    unattempted_question = []
    correct_choices = 0
    unattempted = 0
    wrong_choices = 0
    obtained_marks = 0
    total_marks = 0
    total_questions = 0
    cnt = 0
    
    question_list = []
    for row in freader:
        question_list.append(row)
        total_questions += 1
        total_marks += int(row['marks_correct_ans'])
    
    pattern = re.compile(r"[0-9]+")
    duration = (re.findall(pattern,(freader.fieldnames)[-1]))[0]
    timerTHREAD = threading.Thread(target=runTimer,args=(0,int(duration),0,))
    timerTHREAD.start()
    
    for row in question_list:
        cnt += 1
        print("Question "+row['ques_no']+") "+row['question'])
        print("Option 1) "+row['option1'])
        print("Option 2) "+row['option2'])
        print("Option 3) "+row['option3'])
        print("Option 4) "+row['option4'])
        print("\n")
        print("Credits if Correct Option: "+row['marks_correct_ans'])
        print("Negative Marking: "+row['marks_wrong_ans'])
        
        if row['compulsory'].lower() == 'y':
            print("Is compulsory: YES")
        else:
            print("Is compulsory: NO")
        choice = str(input("Enter Choice: 1, 2, 3, 4, S : S is to skip question  "))
        marked_choice.append(choice)
        
        if temp == -1:
            unattempted = total_questions - correct_choices - wrong_choices
            for i in range(cnt,total_questions+1):
                unattempted_question.append(i)
            break
        
        if choice == row['correct_option']:
            correct_choices += 1
            obtained_marks += int(row['marks_correct_ans'])
        elif choice.upper() == 'S':
            unattempted += 1
            unattempted_question.append(cnt)
        else:
            wrong_choices += 1
            obtained_marks += int(row['marks_wrong_ans'])
      
    print("Press Ctrl+Alt+U to see the unattempted questions")
    print("Press Ctrl+Alt+G to go to your desired question")
    print("Press Ctrl+Alt+F to submit the quiz finally")
    print("Press Ctrl+Alt+E to export the database to csv")

    while temp >= 0:
        pass
    if submitted == 0:
        finalSubmit()
        
    print("Total Quiz Questions:",total_questions)
    print("Total Quiz Questions Attempted:",total_questions-unattempted)
    print("Total Correct Questions:",correct_choices)
    print("Total Wrong Questions:",wrong_choices)
    print("Total Marks: {} / {}".format(obtained_marks,total_marks))
    
    timerTHREAD.join()

def showUnattempted():
    print("Unattempted questions are:",end='  ')
    for x in unattempted_question:
        print("Question {}".format(x),end='  ')
    print("\nPress Esc to exit")
        
def gotoQuestion():
    quesNum = int(input("Enter the question number you want to go to: "))
    row = question_list[quesNum-1]
    print("Question "+row['ques_no']+") "+row['question'])
    print("Option 1) "+row['option1'])
    print("Option 2) "+row['option2'])
    print("Option 3) "+row['option3'])
    print("Option 4) "+row['option4'])
    print("\n")
    print("Credits if Correct Option: "+row['marks_correct_ans'])
    print("Negative Marking: "+row['marks_wrong_ans'])
    
    if row['compulsory'].lower() == 'y':
        print("Is compulsory: YES")
    else:
        print("Is compulsory: NO")
    
    if len(marked_choice) >= quesNum:
        print("Your marked choice is:",marked_choice[quesNum-1])
    else:
        print("You have not attempted this question yet")
    print("\nPress Esc to exit")

def finalSubmit():
    global submitted
    submitted = 1
    path = os.getcwd()
    con = sq3.connect("project1_quiz_cs384.db")
    con.execute('''CREATE TABLE IF NOT EXISTS project1_marks(
        Roll TEXT PRIMARY KEY,
        QuizNum INT,
        Marks INT);''')
    con.commit()
    entry = con.execute("SELECT Roll FROM project1_marks")
    if entry.fetchone() != None:
        con.execute("DELETE FROM project1_marks WHERE Roll=?",(username,))
        con.commit()
    con.execute("INSERT INTO project1_marks VALUES(?,?,?)",(username,quizName,obtained_marks))
    con.commit()
    con.close()
    
    fileToRead = open(path+"\\quiz_wise_questions\\q"+quizNum+".csv","r")
    freader = csv.DictReader(fileToRead)
    fieldnames = freader.fieldnames
    fieldnames[-1] = "marked_choice"
    fieldnames.append("Total")
    fieldnames.append("Legend")
    
    fileToWrite = open(path+"\\individual_responses\\"+quizName+"_"+username+".csv","a",newline='')
    fwriter = csv.DictWriter(fileToWrite, fieldnames)
    fwriter.writeheader()
    cnt = 0 
    for row in freader:
        entry = {"ques_no":row["ques_no"], "question":row["question"],"option1":row["option1"],
                 "option2":row["option2"],"option3":row["option3"],"option4":row["option4"],
                 "correct_option":row["correct_option"],"marks_correct_ans":row["marks_correct_ans"],
                 "marks_wrong_ans":row["marks_wrong_ans"],"compulsory":row["compulsory"],
                 "marked_choice":marked_choice[cnt]}
        if cnt == 0:
            entry["Total"] = correct_choices
            entry["Legend"] = "Correct Choices"
        elif cnt == 1:
            entry["Total"] = wrong_choices
            entry["Legend"] = "Wrong Choices"
        elif cnt == 2:
            entry["Total"] = unattempted
            entry["Legend"] = "Unattempted"
        elif cnt == 3:
            entry["Total"] = obtained_marks
            entry["Legend"] = "Marks Obtained"
        elif cnt == 4:
            entry["Total"] = total_marks
            entry["Legend"] = "Total Quiz Marks"
        fwriter.writerow(entry)
        cnt += 1
    print("\nPress Esc to exit")

def exportDB():
    conn = sq3.connect("project1_quiz_cs384.db")
    entries = conn.execute("SELECT * FROM project1_marks")
    for entry in entries:
        quiz_Name = entry[1]
        rollNo = entry[0]
        marks = entry[2]
        if not os.path.exists(os.getcwd()+"\\quiz_wise_responses\\"+quiz_Name+".csv"):
            qfile = open(os.getcwd()+"\\quiz_wise_responses\\"+quiz_Name+".csv","a",newline='')
            fwriter = csv.DictWriter(qfile, ["roll_number","total_marks"])
            fwriter.writeheader()
            fwriter.writerow({"roll_number":rollNo,"total_marks":marks})
        else:
            qfile = open(os.getcwd()+"\\quiz_wise_responses\\"+quiz_Name+".csv","a",newline='')
            fwriter = csv.DictWriter(qfile, ["roll_number","total_marks"])
            fwriter.writerow({"roll_number":rollNo,"total_marks":marks})
    print("\nPress Esc to exit")
    conn.close()


username = "coder"
response = str(input("Have you registered?\nPress y if Yes or n if No: "))
if response.lower() == 'y':
    flag=login()
else:
    flag=register()

if flag == -1:
    sys.exit()

keyboard.add_hotkey("Ctrl+Alt+U", showUnattempted)
keyboard.add_hotkey("Ctrl+Alt+G", gotoQuestion)
keyboard.add_hotkey("Ctrl+Alt+F", finalSubmit)
keyboard.add_hotkey("Ctrl+Alt+E", exportDB)
    
submitted = 0
nextQuiz = True
while nextQuiz:
    quizNum = str(input("Enter the quiz number you want to attempt from the list below:\n1\n2\n3\n4\n5 "))
    quizName = "Quiz"+quizNum
    print("Roll:",username)
    conn = sq3.connect("project1_quiz_cs384.db")
    dbentry = conn.execute("SELECT Name FROM project1_registration WHERE Username=?",(username,))
    fullname = (dbentry.fetchone())[0]
    conn.close()
    print("Name:",fullname)
    print("Press Ctrl+Alt+U to see the unattempted questions")
    print("Press Ctrl+Alt+G to go to your desired question")
    print("Press Ctrl+Alt+F to submit the quiz finally")
    print("Press Ctrl+Alt+E to export the database to csv")
    submitted = 0
    conductQuiz(quizName, username)
    nextQuiz = str(input("Do you want to attempt more quiz?\nPress y if Yes or n if No: "))
    if nextQuiz == 'y':
        nextQuiz = True 
    else:
        nextQuiz = False
keyboard.wait('esc')
keyboard.unhook_all()