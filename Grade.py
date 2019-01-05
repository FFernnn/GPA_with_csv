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
    data = open_file(f)

    return

def save():
    return

def main_programe():

    while True:
        print("Select mode \n 1.) Edit Grade \n 2.) Calculate Grade")
        select = (input("Your select :"))
        if select == "0":
            break
        elif select == "1":
            print("**** Edit Grade Mode ****")
            show('simple.csv')
        elif select == "2" :
            print("**** Calclate Grade Mode")
            show('simple.csv')
        else:
            print('Try Again !!!')
    return

main_programe()





