flights = [
    {"id": 1, "from": "Hyderabad", "to": "Delhi", "price": 4500, "seats": 5},
    {"id": 2, "from": "Hyderabad", "to": "Mumbai", "price": 3500, "seats": 6},
    {"id": 3, "from": "Bangalore", "to": "Chennai", "price": 3000, "seats": 4},
    {"id": 4, "from": "Delhi", "to": "Kolkata", "price": 5000, "seats": 3}
]
bookings = []
def show_flights():
    print("\nAvailable Flights:")
    print("-" * 60)
    for flight in flights:
        print(f"Flight ID: {flight['id']} | {flight['from']} → {flight['to']} "
              f"| Price: ₹{flight['price']} | Seats: {flight['seats']}")
    print("-" * 60)

def search_flight(source, destination):
    print("\nSearch Results:")
    found = False
    for flight in flights:
        if flight["from"].lower() == source.lower() and flight["to"].lower() == destination.lower():
            print(f"Flight ID: {flight['id']} | Price: ₹{flight['price']} | Seats: {flight['seats']}")
            found = True
    if not found:
        print("No flights found.")


def book_ticket():
    show_flights()
    flight_id = int(input("Enter Flight ID to book: "))
    seats_needed = int(input("Enter number of seats: "))

    for flight in flights:
        if flight["id"] == flight_id:
            if flight["seats"] >= seats_needed:
                name = input("Enter Passenger Name: ")
                total_price = flight["price"] * seats_needed

                booking = {
                    "name": name,
                    "flight": f"{flight['from']} → {flight['to']}",
                    "seats": seats_needed,
                    "total": total_price
                }

                bookings.append(booking)
                flight["seats"] -= seats_needed

                print("\nBooking Successful!")
                print(f"Passenger: {name}")
                print(f"Flight: {flight['from']} → {flight['to']}")
                print(f"Seats Booked: {seats_needed}")
                print(f"Total Amount: ₹{total_price}")
                return
            else:
                print("Not enough seats available.")
                return
    print("Invalid Flight ID.")


def view_bookings():
    if not bookings:
        print("\nNo bookings yet.")
        return

    print("\nYour Bookings:")
    for i, b in enumerate(bookings, start=1):
        print(f"{i}. {b['name']} | {b['flight']} | Seats: {b['seats']} | Total: ₹{b['total']}")


def main():
    while True:
        print("\n  Online Flight Ticket Booking System   ")
        print("1. View Flights")
        print("2. Search Flight")
        print("3. Book Ticket")
        print("4. View Bookings")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_flights()
        elif choice == "2":
            src = input("From: ")
            dest = input("To: ")
            search_flight(src, dest)
        elif choice == "3":
            book_ticket()
        elif choice == "4":
            view_bookings()
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.")


main()
