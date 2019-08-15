import re


directory = dict()

# directory = {'Gurcharan Singh':8146248862,'Naveen Bassi':2345324534,'Jagmanjot Singh':2345676543,'Sresht Shashi':2345676543,'Ankit Billa':3456543223}

# ADD ENTRY function
def addEntry(name, number):
    directory[name] = number

# PRINT DIRECTORY function
def printDirectory():
    for entry in directory:
        print(entry, "-", directory[entry])

# SEARCH ENTRY function
def searchEntry(key,flag):
    str = '[a-zA-Z]*'+key+'[a-zA-Z]*'
    search = re.compile(str, re.IGNORECASE)

    if flag == False:
        names = dict()
        for entry in directory:
            if search.findall(entry):
                names[entry] = directory[entry]
        return names

    else:
        names = []
        for entry in directory:
            if search.findall(entry):
                names.append(entry)
        return names

# REMOVE ENTRY function
def removeEntry(name):
    entries = searchEntry(name,True)
    if entries is None:
        return None
    elif type(entries) != list:
        del directory[entries]
        return 1
    index = 1
    for entry in entries:
        print(index,'.', entry)
        index += 1
    index -= 1
    val = int(input('Which Entry to Delete?:'))
    if val > index or val < 0:
        print('Invalid Input')
        return None
    else:
        del directory[entries[val-1]]
        return 1
    
# UPDATE ENTRY function
def updateEntry(name,number):
    entries = searchEntry(name,True)
    if entries is None:
        return None
    elif type(entries) != list:
        directory[entries] = number
        return 1
    index = 1
    for entry in entries:
        print(index,'.', entry)
        index += 1
    index -= 1
    val = int(input('Which Entry to Update?:'))
    if val > index or val < 0:
        print('Invalid Input')
        return None
    else:
        directory[entries[val-1]] = number
        return 1


# MAIN 
if __name__ == "__main__":
    print("TELEPHONE DIRECTORY")
    print('Actions : ')

    while(True):
        print('1. Add Entry \n 2. Remove Entry \n 3. Update Entry \n 4. Search \n 5. Print All Entries \n 6. Exit')

        
        choice = input('What do you want to do ? ')

        if choice == '1':
            name = input('Enter Contact Name:')
            number = input('Enter Contact Number:')
            addEntry(name,number)
        elif choice == '2':
            name = input('Enter full Contact Name:')
            value = removeEntry(name)
            if value is None:
                print('The Entry does not exist')
            else:
                print('Entry Removed')
        elif choice == '3':
            name = input('Enter Key:')
            number = input('Enter Number:')
            val = updateEntry(name,number)
            if val is None:
                print('The Entry does not exist')
            else:
                print('Entry Updated')
        elif choice == '4':
            key = input('Enter Key to search:')
            names = searchEntry(key,False)
            for name in names:
                print(name,'-',names[name])
        elif choice == '5':
            printDirectory()
        elif choice == '6':
            break
        else:
            print('---Invalid Input---')
