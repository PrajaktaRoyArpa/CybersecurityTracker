from manager import IncidentManager

def main():
    manager = IncidentManager()

    while True: 
        print("Cybersecurity Incident Tracker")
        print("1. Create Incident")
        print("2. List Incidents")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter incident title: ")
            attack_type = input("Enter attack type: ")
            severity = input("Enter severity (Low/Medium/High): ")
            incident =manager.create_incident(title, attack_type, severity)
            print("Incident has been created successfully!")
        
        elif choice == "2":
            manager.list_incidents()
        
        elif choice == "3":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()