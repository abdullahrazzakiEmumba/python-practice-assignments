import csv
try:
    address_book = []
    while True:
        try:
            choice = int(input("Please select one option:\n1. Add Contact\n2. Search Contact\nEnter: "))
        except:
            print("Invalid choice")
        if choice==1:
            name = input("Enter name: ")
            phone_number = input("Enter phone number:")
            address_book.append({
                "name":name,
                "phone_number":phone_number
            })
        elif choice==2:
            name = input("Enter name to search: ")
            contact = [c for c in address_book if name.lower() in c.get('name','').lower()]
            contact = contact[0] if len(contact)>0 else False
            if contact:
                print("Name:",contact.get("name"),"\nPhone:",contact.get("phone_number"))
            else:
                print("No match found")
        choice = input("Do you want to continue? (y/n): ")
        if choice=='n':
            break
        
except Exception as e:
    print(e)