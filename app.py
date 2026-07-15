def add_student():
    try:
        r = int(input("\nEnter roll number: "))
        name = input("Enter student name: ")
        mobile = int(input("Enter mobile number: "))
        
        students[r] = {
            "name" : name ,
            "mobile" : mobile ,
        }
        print("Enter marks for the student")
        math = int(input("Enter maths mark : "))
        phy = int(input("Enter phy mark : "))
        che = int(input("Enter che mark : "))
        marks[r] = {
            "math": math,
            "phy" :  phy,
            "che" : che }
        
        print("Student details added successfully")
    except:
        print("Enter valid details")
def view_student():
    print("\n Student Details")
    print()
    for r,student in students.items():
        print("Student rollnumber :" , r)
        for key,value in student.items():
            print(key,":",value)
        print("Student marks")
        for k,v in marks[r].items():
            print(k,":",v)


def search_student():
    try:
        n = int(input("\nEnter roll number: "))
        if n in students.keys():
            print("Student rollnumber :" , n)
            for key,value in students[n].items():
                print(key,":",value)
            print("Student marks")
        for k,v in marks[n].items():
            print(k,":",v)
    except:
        print("Enter valid roll number")
def delete_student():
    try:
        n = int(input("\nEnter roll number: "))
        if n in students.keys():
            del students[n]
            print("Deleted successfully")
        else:
            print("Student roll number does not exist")
    except:
        print("Enter valid roll number ") 
def update_student():
    try :
        n = int(input("\nEnter student roll number :" ))
        xx = input("Enter what you want to update general details or marks [type -> (general/marks)]").lower()
        if xx == "general":
          if n in students.keys():
            for key,value in students.items():
                if key == n:
                    print("What detail you wish to change ? ")
                    for i in value.keys():
                        print(i)
                    detail = input("Enter the field you want to change : ").lower()
                    x = input(("Enter the value to be saved")).lower()
                    if detail == "mobile":
                        students[n][detail] = int(x)
                    else:
                        students[n][detail] = x
                    break
            print("Student general details updated")
          else:
            print("student does not exist")
        elif xx == "marks":
            for k,v in marks[n].items():
                print(k,":",v)
            sub = input("Enter which subject").lower()
            try:
                val = int(input("Enter value to be replaced"))
            except:
                print("Enter valid marks")
            marks[n][sub] = val
            print("Marks update successfully")
            
    except:
        print("Enter valid roll number")


def status():
    n = int(input("\nEnter student roll number : "))
    m = marks[n]
    sum = 0
    for k,v in m.items():
        sum += v
    if sum//3  <= 50:
        print("Bad")
    elif sum//3 >= 50 and sum//3 <= 150:
        print("Average")
    elif sum >= 150 and sum <= 250:
        print("Good")
    elif sum >= 250 and sum <= 300:
        print("Best")

students = {}
marks = {}

while True:
    try :
        n = int(input("\nEnter your choice : "))
        if n == 1:
            add_student()
        elif n == 2:
            view_student()
        elif n == 3:
            search_student()
        elif n == 4:
            delete_student()
        elif n == 5:
            update_student() 
        elif n == 6:
            status()
        else:
            break

    except:
        print("Enter valid number ")


   

