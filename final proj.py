#print the title of project
print("*"*35,"\n***** List of students' notes *****",end="\n")
print("*"*35)
#####################
import sqlite3
vt=sqlite3.connect("C:\sqlite\database.db")
im=vt.cursor()
tabl="create table students_scores(name text,surname text,TC integer,score integer)"
im.execute(tabl)
tabb=im.fetchall()
vt.commit()
sc=[]                # List of scores
def med(group,lst):  # Calculate the percent of a group
    return len(group)*100/len(lst)
def a(s):            # Allow typing only characters
    if s.isalpha():
        return True
    return False
def num(x):          # Allow typing numbers only
    try:
        a=int(x)
    except ValueError:
        print("Invalide value,",end="")
        return False
    return True

def scor(j):        # Allow enteringa number between 0-100
    if int(j)<0 or int(j)>100:
        return False

en="y"    # if user need to enter another student's information
while en=="y":
######################### Enter student's name
    print("enter a name:",end="")
    nam=input(" ")
    while a(nam)==False:
        nam=input("error again:")
        a(nam)
        if a(nam)==True:
            break
######################## Enter student's surname
    print("enter a surname:",end="")
    surnam=input(" ")
    while a(surnam)==False:
        surnam=input("error again:")
        a(surnam)
        if a(surnam)==True:
            break
######################## Enter student's TC number
    tcno=input("enter no")
    while num(tcno)==False or len(tcno)!=11:
        tcno=input("enter again:")
        if num(tcno)==True:
            if len(tcno)==11:
                break
            else:
                print("TC no must be 11 digit,",end="")
######################## Enter student's score
    sco=input("Please enter score:")
    while num(sco)==False or scor(sco)==False:
        sco=input("enter again:")
        if num(sco)==True:
            if scor(sco)!=False:
                break
            else:
                print("Score must be between 0 and 100,",end="")
######################## Filling list with scores and table with information
    sc.append(int(sco))
    stu="insert into students_scores(name,surname,TC,score) values(?,?,?,?)"
    valu=(nam,surnam,tcno,sco)
    im.execute(stu,valu)
    vt.commit()
    en=input("would you like to insert another information?y/n")
    while en!="y" and en!="n":
        en=str(input("please enter y or n:"))
####################### Creating lists upon scores
a=[i for i in sc if i>=90]
b=[i for i in sc if i>=80 and i<90]
c=[i for i in sc if i>=70 and i<80]
d=[i for i in sc if i>=60 and i<70]
f=[i for i in sc if i<60]
####################### Printing results
print("*"*40)
j=16
for i in range(1,40,8):
    print(" "*j,"*"*i)
    j-=4
print(" ***    score |   X>=90  | A   ***")
print(" ***    score | 90>X>=80 | B   ***")
print(" ***    score | 80>X>=70 | C   ***")
print(" ***    score | 70>X>=60 | D   ***")
print(" ***    score |   60>X   | F   ***")
print("","*"*33)

print("Number of succeed students: ",len(a)+len(b)+len(c)+len(d))
print("Number of failed students: ",len(f))
print("Percent of succeed students: ",100-(len(f)*100/len(sc)))
print("Highest score: ",max(a))
print("Lowest score: ",min(f))
print("","*"*33)
print("No. of A:",int(med(a,sc)),"%:","="*int(med(a,sc)))
print("No. of B:",int(med(b,sc)),"%:","="*int(med(b,sc)))
print("No. of C:",int(med(c,sc)),"%:","="*int(med(c,sc)))
print("No. of D:",int(med(d,sc)),"%:","="*int(med(d,sc)))
print("No. of F:",int(med(f,sc)),"%:","="*int(med(f,sc)))
print("","*"*33)
ja=33
for i in range(0,17,4):
    print(" "*i,"*"*ja)
    ja-=8

