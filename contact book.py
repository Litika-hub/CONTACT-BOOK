contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print("Contact Added Successfully!")

def view_contacts():
    if not contacts:
        print("No Contacts Found!")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"{name} - {details['Phone']}")

def search_contact():
    search = input("Enter Name or Phone Number: ")
    found = False

    for name, details in contacts.items():
        if search == name or search == details["Phone"]:
            print("\nContact Found:")
            print("Name:", name)
            print("Phone:", details["Phone"])
            print("Email:", details["Email"])
            print("Address:", details["Address"])
            found = True

    if not found:
        print("Contact Not Found!")

def update_contact():
    name = input("Enter Contact Name to Update: ")

    if name in contacts:
        contacts[name]["Phone"] = input("New Phone: ")
        contacts[name]["Email"] = input("New Email: ")
        contacts[name]["Address"] = input("New Address: ")
        print("Contact Updated Successfully!")
    else:
        print("Contact Not Found!")

def delete_contact():
    name = input("Enter Contact Name to Delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found!")

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Try Again.")