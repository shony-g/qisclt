import csv


""" List All Records """
def show_records():
    print("You have selected List all records:")
    with open ('sdap.csv', 'r')as f:
        abb = csv.reader(f)

        for x in abb:
            print(x)

""" Add Record """
def add_records():
    print("You have selected Add Record:")
    Uname = input("Enter name:")
    Pnumber = input("Enter Phone number (+91XXXXXXXXXX):")
    PnumberCh = input("Add more phone? 1-Yes / 0-No:")
    if PnumberCh == "1":
        Pnumber2 = input("Enter Phone number (+91XXXXXXXXXX):")
    else:
        Pnumber2 = ""
    Uemail = input("Enter email id:")
    UemailCh = input("Add more email? 1-Yes / 0-No:")
    if UemailCh =='1':
        Uemail2 = input("Enter email id:")
    else:
        Uemail2 =""
    print("Record added successfully 👍")

    with open ("sdap.csv",'a', newline="") as f:
        abb = csv.writer(f)
        abb.writerow([Uname,Pnumber,Pnumber2,Uemail,Uemail2])

""" Edit Record """

def edit_records():
    print("You have selected Edit Record:")

    Uname = input("Enter name to edit:")
    rows = []
    flag = 0

    with open("sdap.csv", "r", newline="") as f:
        abb = csv.DictReader(f)
        fieldnames = abb.fieldnames

        for x in abb:
            if x["Name"] == Uname:
                flag = 1

                choiNum = input("Edit options? 1 - Name, 2 - Phone number, 3 - Email, 0 - Exit: ")

                if choiNum == "1":
                    x["Name"] = input("Enter the new name:")
                    print("Record updated successfully 👍")

                elif choiNum == "2":
                    print(f"Primary Ph: {x['Phone Number']} and Secondary Ph: {x['Sec Phone number']}")
                    PnumberCh = input("For Primary Ph - 1 / For Secondary Ph - 2:")

                    if PnumberCh == "1":
                        x["Phone Number"] = input("Enter Phone number (+91XXXXXXXXXX):")
                        print("Record updated successfully 👍")
                    elif PnumberCh == "2":
                        x["Sec Phone number"] = input("Enter Phone number (+91XXXXXXXXXX):")
                        print("Record updated successfully 👍")
                    else:
                        print("Not valid input")

                elif choiNum == "3":
                    print(f"Primary Email: {x['Email Address']} and Secondary Email: {x['Sec Email ID']}")
                    emailCh = input("For Primary Email - 1 / For Secondary Email - 2:")

                    if emailCh == "1":
                        x["Email Address"] = input("Enter Primary Email:")
                        print("Record updated successfully 👍")
                    elif emailCh == "2":
                        x["Sec Email ID"] = input("Enter Secondary Email:")
                        print("Record updated successfully 👍")
                    else:
                        print("Not valid input")

                elif choiNum == "0":
                    print("Exiting edit menu...")

                else:
                    print("Not valid input")

            rows.append(x)

    if flag == 0:
        print("No such Name")
        return

    with open("sdap.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    

""" Delete Record """
def delete_records():
    print("You have selected Delete Record:")

    Uname = input("Enter name to delete:")
    rows = []
    flag = 0

    with open("sdap.csv", "r", newline="") as f:
        abb = csv.DictReader(f)
        fieldnames = abb.fieldnames

        for x in abb:
            if x["Name"] == Uname:
                flag = 1
            else:
                rows.append(x)

    if flag == 0:
        print("No such Name")
        return

    with open("sdap.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Record deleted successfully 👍")

""" Creating menu which shows continuously until the user chooses Exit"""

while True:
    print("\n<---------------- Menu ------------------->")
    print("1. List all records")
    print("2. Add Record")
    print("3. Edit Record")
    print("4. Delete Record")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_records()
        
    elif choice == "2":
        add_records()

    elif choice == "3":
        edit_records()

    elif choice == "4":
        delete_records()

    elif choice == "0":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")

