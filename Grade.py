import csv

def open_file(f):
    subject = []
    with open(f, newline='') as csvfile:
          reader = csv.DictReader(csvfile)
          for row in reader:
              subject.append([row['TERM'],row['SUBJECT'], (row['CREDIT']), (row['GRADE'])])
    return subject

def show(f):
    data = open_file(f)
    t = 'Term'
    s = 'Subject'
    c = 'Credit'
    g = 'Grade'
    print(' -----------------------Your grade-----------------------')
    print(t.ljust(10) + s.ljust(25) + c.ljust(10) + g)
    print('---------------------------------------------------------')
    for i in range(len(data)):
        print((data[i][0]).ljust(10) + (data[i][1]).ljust(27) + (data[i][2]).ljust(10) + (data[i][3]) )
    print('---------------------------------------------------------')
    print("GPA : {:.2f}".format(calculate(data)))
    print('---------------------------------------------------------')

def convert_grade(intput_key):
    grade = {'A': 4,
             'B+': 3.5,
             'B': 3,
             'C+': 2.5,
             'C': 2,
             'D+': 1.5,
             'D': 1,
             'F': 0}
    return grade[intput_key]

def calculate(data):
    total_c = 0
    total_CxG = 0
    for i in range(len(data)):
        total_c += float(data[i][2])
        total_CxG += (float(data[i][2])*float(convert_grade(data[i][3])))
    GPA = total_CxG / total_c
    return GPA

def edit(f):
    show(f)
    data = open_file(f)
    print("Select mode \n 1.) edit grade \n 2.) add subject")
    x = int(input("Your select :"))
    if x == 1:
        print('How many subject to change grade ?')
        intput_choose = int(input("You want to change :"))
        for i in range(intput_choose):
            select_sub = input("Select subject{} : ".format(i+1))
            new_grade = input("New Grade : ")
            # select subject
            for i in range(len(data)):
                if select_sub == str(data[i][1]):
                    data[i][3] = new_grade

    elif x == 2:
        print("How many to add subject ?")
        add_input = int(input("Your want to add : "))
        for i in range(add_input):
            new_term = input("Term :")
            new_subject = input("Subject : ")
            new_credit = input("Credit :")
            new_grade = input("Grade :")
            data.append([new_term,new_subject,new_credit,new_grade])
    # new GPA
    total_c = 0
    total_CxG = 0
    for i in range(len(data)):
        total_c += float(data[i][2])
        total_CxG += (float(data[i][2]) * float(convert_grade(data[i][3])))
    GPA = total_CxG / total_c
    print('New GPA : {:.2f}'.format(GPA))
    print('You want to save change ? [Y/N]')
    choice = input('you choose : ')
    if choice == 'Y' or 'y':
        save(data)
    return

def save(data):
    name_file =input("File name :")
    with open(name_file, "w", newline="") as csvfile:
        fieldnames = ['Term','Subject','Credit','Grade']
        fw = csv.DictWriter(csvfile, fieldnames=fieldnames)
        fw.writeheader()
        for i in range(len(data)):
            fw.writerow({'Term':data[i][0],
                         'Subject':data[i][1],
                         'Credit':data[i][2],
                         'Grade':data[i][3]})
    print("Save Success !!!")
    return

def main_programe():
    print("Select your term [ex. 1/1]")
    while True:
        select_term = (input("Your term :"))
        if select_term == "1/1":
            print("Select mode \n 1.) Edit Grade \n 2.) Calculate Grade")
            select = (input("Your select :"))
            if select == "1":
                print("**** Edit Grade Mode ****")
                edit("term/TERM1-1.csv")
            elif select == "2":
                print("**** Calclate Grade Mode ****")
                show("term/TERM1-1.csv")

        elif select_term == "1/2":
            print("Select mode \n 1.) Edit Grade \n 2.) Calculate Grade")
            select = (input("Your select :"))
            if select == "1":
                print("**** Edit Grade Mode ****")
                edit("term/TERM1-2.csv")
            elif select == "2":
                print("**** Calclate Grade Mode ****")
                show("term/TERM1-2.csv")

        elif select_term == "2/1":
            print("Select mode \n 1.) Edit Grade \n 2.) Calculate Grade")
            select = (input("Your select :"))
            if select == "1":
                print("**** Edit Grade Mode ****")
                edit("term/TERM2-1.csv")
            elif select == "2":
                print("**** Calclate Grade Mode ****")
                show("term/TERM2-1.csv")

        elif select_term == "2/2":
            print("Select mode \n 1.) Edit Grade \n 2.) Calculate Grade")
            select = (input("Your select :"))
            if select == "1":
                print("**** Edit Grade Mode ****")
                edit("term/TERM2-2.csv")
            elif select == "2":
                print("**** Calclate Grade Mode ****")
                show("term/TERM2-2.csv")

        elif select_term == "3/1":
            print("Select mode \n 1.) Edit Grade \n 2.) Calculate Grade")
            select = (input("Your select :"))
            if select == "1":
                print("**** Edit Grade Mode ****")
                edit("term/TERM3-1.csv")
            elif select == "2":
                print("**** Calclate Grade Mode ****")
                show("term/TERM3-1.csv")

        elif select_term == "3/2":
            print("coming soon")

        elif select_term == "4/1":
            print("coming soon")

        elif select_term == "4/2":
            print("coming soon")

        else:
            print("Try again !!!!!")


main_programe()





