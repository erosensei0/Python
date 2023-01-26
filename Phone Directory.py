
print("WELCOME TO KIRAN'S PhONE DIRECTORY")
contacts = {
   
}

def showMenu():
    print("What do you want to do?")
    print("1. View contact")
    print("2. Edit contact")
    print("3. Add contact")
    print("4. Delete contact")
    print("5. Exit")

    selectMenu()

def selectMenu():
    repeat = True
    while repeat == True:
        try:
            option = int(input("Choose[1-5]: "))
        except ValueError:
            print("Please input number.")
            option = 0
        if option > 0 and option < 6: repeat = False
        if option == 1:
            showContacts()
            showMenu()
        elif option == 2:
            print("\n==============")
            print("Change Contact")
            print("==============")
            updateContact()
            showMenu()
        elif option == 3:
            print("\n===========")
            print("Add Contact")
            print("===========")
            addContact()
            showMenu()
        elif option == 4:
            deleteContact()
            showMenu()
        elif option == 5:
            print("Good bye!")
            break
        else: 
            print("Option unavailable.")

def showContacts():
  
    num = 1
   
    print("|No.| Name            | Number           | Address:                            |")
    
    for contact in contacts.values():
        
        print("|{no} .| {name:<15} | {number:<15}  | {address:<35} |"
        .format(no = num, name = contact["name"], 
                number = contact["number"], address = contact["address"]))
        num += 1
    

def addContact():

    if(contacts.keys()):
        contact_order = list(contacts.keys())[-1] + 1
    else:
        contact_order = 0

  
    while True:
        try:
            name = str(input("Enter contact name: "))
            number = int(input("Enter contact number: "))
            address = str(input("Enter contact address: "))
         
            contacts[contact_order] = {
                "name" : "{}". format(name),
                "number" : number,
                "address" : "{}".format(address)
            }
            print("Data " + name + " added succesfully!\n")
            break
        except ValueError:
            print("Wrong input. Please enter a correct format.\n")
            break

def updateContact():
    isUpdate = False
    showContacts()

    oldName = str(input("Enter contact name you want to change: "))

    for contact in contacts.values():
        if oldName in contact.values():
            print("Data " + oldName + " found!")
            try:
                newName = str(input("Enter contact new name: "))
                newNumber = int(input("Enter contact number: "))
                newAddress = str(input("Enter contact address: "))
           
                contact.update({"name" : "{}". format(newName)})
                contact.update({"number" : newNumber})
                contact.update({"address" : "{}". format(newAddress)})
                isUpdate = True
                print("Data '{}' succesfully changed to '{}'.\n".format(oldName, newName))
                
            except ValueError:
                print("Format error. Please enter a correct number.") 

    if isUpdate == False:
        print("Data not found. Please enter a correct name\n")
        showMenu()

def deleteContact():
    isDelete = False
    showContacts()
    name = str(input("Enter contact's name you want to delete: "))
    for contact_id, contact_info in list(contacts.items()):
        if contact_info["name"] == name:
            del contacts[contact_id]
            showContacts()
            print("Data '{}' deleted Succesfully!\n".format(name))
            isDelete = True
    if isDelete == False: print("Data not found!\n")


showMenu()