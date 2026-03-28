from manager import IncidentManager
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

console = Console()

def print_menu():
    console.print(Rule("[bold cyan]CYBERSECURITY INCIDENT TRACKER[/bold cyan]"))
    console.print("[cyan]1.[/cyan] Create Incident")
    console.print("[cyan]2.[/cyan] List Incidents")
    console.print("[cyan]3.[/cyan] Update Incident Status")
    console.print("[cyan]4.[/cyan] Delete Incident")
    console.print("[cyan]5.[/cyan] Search Incidents")
    console.print("[cyan]6.[/cyan] Severity Report")
    console.print("[cyan]7.[/cyan] Exit")
    console.print()

def main():
    manager = IncidentManager()
    manager.load_file()

    console.print(Panel.fit(
    "[bold red]CyberShield CLI[/bold red]",
    border_style="red",
    padding=(0, 30)
))
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            console.print(Rule("[green]New Incident[/green]"))
            title = input("Enter incident title: ").strip()
            attack_type = input("Enter attack type: ").strip()
            severity = input("Enter severity (Low/Medium/High): ").strip()

            if not title or not attack_type or not severity:
                console.print("[red]All fields are required.[/red]")
                continue

            incident = manager.create_incident(title, attack_type, severity)
            if incident:
                console.print(f"[green] Incident #{incident.incident_id} created successfully![/green]")

        elif choice == "2":
            manager.list_incidents()

        elif choice == "3":
            console.print(Rule("Update Status"))
            incident_id = input("Enter incident ID: ").strip()

            if not incident_id.isdigit():
                console.print("[red]Invalid input. Please enter a numeric ID.[/red]")
                continue

            new_status = input("Enter new status (Open/Resolved/Closed): ").strip()
            success = manager.update_status(int(incident_id), new_status)

            if success:
                console.print("[green]Incident updated successfully![/green]")
            else:
                console.print("[red]Incident ID not found.[/red]")

        elif choice == "4":
            console.print(Rule("[red]Delete Incident[/red]"))
            incident_id = input("Enter incident ID: ").strip()

            if not incident_id.isdigit():
                console.print("[red]Invalid input. Please enter a numeric ID.[/red]")
                continue

            confirm = input("Are you sure you want to delete? (yes/no): ").strip().lower()
            if confirm != "yes":
                console.print("Deletion cancelled.")
                continue

            success = manager.delete_incident(int(incident_id))
            if success:
                console.print("[green]Incident deleted successfully![/green]")
            else:
                console.print("[red]Incident ID not found.[/red]")

        elif choice == "5":
            console.print(Rule("[magenta]Search Incidents[/magenta]"))
            keyword = input("Keyword to search (or leave blank): ").strip()
            severity = input("Filter by severity (Low/Medium/High or blank): ").strip()
            results = manager.search_incidents(
                keyword  if keyword  else None,
                severity if severity else None
            )
            manager.display_incidents(results)

        elif choice == "6":
            manager.display_report(manager.generate_report())

        elif choice == "0":
            manager.save_file()
            console.print("\n[bold red]Data has been saved. Stay secured and goodbye! [/bold red]\n")
            break

        else:
            console.print("[red]Invalid choice. Please try again.[/red]")

if __name__ == "__main__":
    main()
