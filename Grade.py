import csv

def open_file(f):
    subject = []
    with open(f, newline='') as csvfile:
          reader = csv.DictReader(csvfile)

          for row in reader:

              subject.append([row['SUBJECT'], (row['CREDIT']), (row['GRADE'])])
    return subject

def show(f):
    data = open_file(f)
    s = 'Subject'
    c = 'Credit'
    g = 'Grade'
    print(' -----------------------Your grade-----------------------')
    print(s.ljust(30) + c.ljust(34) + g)
    print('---------------------------------------------------------')
    for i in range(len(data)):
        print((data[i][0]).ljust(32) + (data[i][1]).ljust(34) + data[i][2] )
    print('---------------------------------------------------------')
    print("GPA : {:.2f}".format(calculate(f)))
    print('---------------------------------------------------------')

def calculate(f):
    data = open_file(f)
    total_c = 0
    total_CxG = 0
    for i in range(len(data)):
        total_c += float(data[i][1])
        total_CxG += (float(data[i][1])*float(data[i][2]))
    GPA = total_CxG / total_c
    return GPA

def edit(f):
    show(f)
    data = open_file(f)
    print('How many to change subject ?')
    intput_choose = int(input("You want to change :"))
    for i in range(intput_choose):
        select_sub = input("Select subject{} : ".format(i+1))
        new_grade = input("New Grade : ")
        # select subject
        for i in range(len(data)):
            if select_sub == str(data[i][0]):
                data[i][2] = new_grade

    # new GPA
    total_c = 0
    total_CxG = 0
    for i in range(len(data)):
        total_c += float(data[i][1])
        total_CxG += (float(data[i][1]) * float(data[i][2]))
    GPA = total_CxG / total_c
    print('New GPA : {:.2f}'.format(GPA))

    print('You want to save change ? [Y/N]')
    choice = input('you choose : ')
    if choice == 'N' or 'n':
        return data
    elif choice == 'Y' or 'y':
        save(data)

    return data

def save(data):
    with open("new.csv", "w", newline="") as csvfile:
        fieldnames = ['Subject','Credit','Grade']
        fw = csv.DictWriter(csvfile, fieldnames=fieldnames)
        fw.writeheader()
        for i in range(len(data)):
            fw.writerow({'Subject':data[i][0],
                         'Credit':data[i][1],
                         'Grade':data[i][2]})
    print("Save Success !!!")
    return

def main_programe(f):

    while True:
        print("Select mode \n 1.) Edit Grade \n 2.) Calculate Grade")
        select = (input("Your select :"))
        if select == "0":
            print('GOOD BYE')
            break
        elif select == "1":
            print("**** Edit Grade Mode ****")
            edit(f)

        elif select == "2" :
            print("**** Calclate Grade Mode")
            show(f)
        else:
            print('Try Again !!!')
    return

main_programe("simple.csv")





