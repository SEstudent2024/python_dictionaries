# 2. Python Programming Challenges for Customer Service Data Handling
# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and 
# loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Open a new service ticket.

def open_ticket(ticket_id, customer, issue):
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
    print(f"New Ticket '{ticket_id}' for {customer} added successfully.")

# Update the status of an existing ticket.

def update_ticket_status(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
        print(f"Ticket '{ticket_id}' not found.")

# Display all tickets or filter by status.

def display_tickets(filter_status=None):
    if filter_status:
        print(f"\nDisplaying {filter_status} tickets:")
        for ticket_id, details in service_tickets.items():
            if details["Status"].lower() == filter_status.lower():
                print(f"{ticket_id}: {details}:")
    else:
        print('\nDisplaying all tickets:')
        for ticket_id, details in service_tickets.items():
            print(f"{ticket_id}: {details}")

# Initialize with some sample tickets and include functionality for additional ticket entry.

def main():
    while True:
        print("\nCustomer Service Ticket Tracket")
        print("1. Open a new service.")
        print("2. Update the status of an exixting ticket.")
        print("3. Display all tickets")
        print("4. Display ticket by status")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            ticket_id = input("Enter ticket ID: ")
            customer = input("Enter customer name: ")
            issue = input("Enter isssue description: ")
            open_ticket(ticket_id, customer, issue)

        elif choice == "2":
            ticket_id = input("Enter ticket ID: ")
            status = input("Enter new status (open/close): ") 

        elif choice == "3":
            display_tickets()

        elif choice == "4":
            status = input("Enter status to filter by (open/closed): ")

        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

