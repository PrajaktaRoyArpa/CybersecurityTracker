
from manager import IncidentManager

def main():
    manager = IncidentManager()

    while True: 
        print("Cybersecurity Incident Tracker")
        print("1. Create Incident")
        print("2. List Incidents")
        print("3. Update Incident status")
        print("4. Delete Incident")
        print("5. Search Incidents")
        print("6. Exit")        
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
            try: 
                incident_id = int (input("Enter incident ID: "))
                new_status = input("Enter new status (open/resolved/closed): ")
                success = manager.update_status(incident_id, new_status)
                if success: 
                    print("Status updated successfully!")
                else:
                    print("Incident not found.")

            except ValueError:
                print("Invalid input. Please enter a valid incident ID.")
        
        elif choice == "4":
            try:
                incident_id = int(input("Enter incident ID to delete: "))
                success = manager.delete_incident(incident_id)
                if success:
                    print("Incident deleted successfully!")
                else:
                    print("Incident not found.")
            except ValueError:
                print("Invalid input. Please enter a valid incident ID.")
        
        elif choice == "5":
            keyword = input("Enter keyword to search or leave blank to skip: ")
            severity = input("Enter severity to filter (Low/Medium/High/leave blank to skip): ")
            status = input("Enter status to filter (open/resolved/closed/leave blank to skip): ")
            results = manager.search_incidents(keyword if keyword else None, severity if severity else None)
            if results:
                manager.display_custom_list(results)
            else:
                print("No matching incidents found.")
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
