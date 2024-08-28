# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:

# Open a new service ticket.

def new_ticket (ticket_system, ticket_number, name, issue, status):
    if ticket_number not in ticket_system:
        ticket_system[ticket_number]={"Customer": name, "Issue": issue, "Status": status}
        return print(f"{name} your ticket for:\n{issue}\nis now {status}!")
    else:
        return print(f"{ticket_number} already exists. Please choose another option.")

# Update the status of an existing ticket.

def check_status(ticket_system, ticket_number):
    if ticket_number in ticket_system:
        current_status = ticket_system[ticket_number]["Status"]
        return print(f"{ticket_number} is {current_status}")
    else:
        return print(f"{ticket_number} is not in the system. Please try again.")

# Display all tickets or filter by status.

def display_tickets(ticket_system):
    for ticket_number, categories in ticket_system.items():
        print (f"{ticket_number} has the following information:")
        for category, info in categories.items():
            print (f"{category}: {info}")



# Initialize with some sample tickets and include functionality for additional ticket entry.

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

while True:
    user_request = input ("Which option would you like to perform?:\n-Add a Ticket\n-Check Ticket Status\n-Display Tickets\n-Quit\n").lower
    if user_request() == "quit":
        break
    elif user_request() == "add a ticket":
        user_ticket_number = input ("Enter your own custom ticket number\n(write it down for future reference when checking status): ")
        user_name = input ("What's your name?\n")
        user_issue = input ("What type of issue are you facing?\n(ex. Forgotten Password, Login Problem, Payment Issue, etc)\n")
        new_ticket (service_tickets, user_ticket_number, user_name, user_issue, "open")
    elif user_request() == "check ticket status":
        ticket_to_check = input ("What is your ticket number?\n")
        check_status (service_tickets, ticket_to_check)
    elif user_request () == "display tickets":
        display_tickets (service_tickets)
    else:
        print ("Invalid entry. Please type an option as listed.\n(Not Case Sensitive)")