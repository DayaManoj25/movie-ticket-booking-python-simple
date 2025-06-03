import mysql.connector as sql

# Connect to MySQL database
conn = sql.connect(host='localhost', user='root', passwd='#234Daya')
cursor = conn.cursor()
cursor.execute("USE CSproject")

if conn.is_connected():
    print("*******************************************************************")
    print("*********** THE GRANDEUR MULTIPLEX CINEMAS TICKET BOOKING ***********")
    print("*******************************************************************\n")

    print("*******************************************************************")
    print("1. Tickets are required for children aged 3 years and above.")
    print("2. Tickets once purchased cannot be exchanged, adjusted, or transferred for any other show.")
    print("3. Laptops, tablets, cameras, and all other electronic items are not allowed inside cinema premises.")
    print("4. Smoking and alcohol consumption are strictly prohibited.")
    print("5. The cinema reserves the right of admission.")
    print("6. Items like carry-bags, eatables, helmets, and handbags are not allowed inside the theatres.")
    print("7. For 3D movies, the ticket price includes charges for usage of 3D glasses.")
    print("8. Patrons with fever or symptoms such as cough will not be allowed entry.")
    print("9. Wearing masks is mandatory.")
    print("*******************************************************************\n")

print("------------------------------------------------------------")
print("ENTER MOVIE DETAILS")
print("------------------------------------------------------------")
print("*Available Movies*")
print("+++++++++++++++++++++++++++++++++++++++")
print("Screen 1 : Bheeshma Parvam - MovieID : 101")
print("Screen 2 : Naaradan - MovieID : 102")
print("Screen 3 : Gangubhai Kathiawadi - MovieID : 103")
print("Screen 4 : The Batman (3D) - MovieID : 104")
print("Screen 5 : Hey Sinamika!! - MovieID : 105")
print("Screen 6 : Bheemla Nayak - MovieID : 106")
print("+++++++++++++++++++++++++++++++++++++++\n")

valid_movie_ids = [101, 102, 103, 104, 105, 106]
movie_id = int(input("Enter movie id : "))
print('')

movie_details = {
    101: "BHEESHMA PARVAM - Rating : 92%",
    102: "NAARADAN - Rating : 68%",
    103: "GANGUBHAI KATHIAWADI - Rating : 82%",
    104: "THE BATMAN (3D) - Rating : 85%",
    105: "HEY SINAMIKA!! - Rating : 79%",
    106: "BHEEMLA NAYAK - Rating : 81%"
}

if movie_id not in valid_movie_ids:
    print("Movie ID not available.")
    exit()

movie_name = movie_details[movie_id]
print("------------------------------------------------------------")
print("Movie : ", movie_name)
print("------------------------------------------------------------")

movie_date = input("Enter the date to watch the movie (YYYY-MM-DD) : ")
print('')

# Time slots for each movie in 12-hour format without "pm" (to avoid confusion)
time_slots = {
    101: ["09:00 AM", "11:45 AM", "02:30 PM", "05:45 PM", "09:00 PM", "11:00 PM"],
    102: ["10:30 AM", "01:00 PM", "03:45 PM", "05:00 PM", "10:00 PM"],
    103: ["07:15 AM", "10:45 AM", "02:00 PM", "11:00 PM"],
    104: ["10:00 AM", "11:45 AM", "01:30 PM", "03:45 PM", "09:30 PM", "11:00 PM"],
    105: ["10:30 AM", "02:30 PM", "09:00 PM"],
    106: ["11:30 AM", "03:45 PM", "08:00 PM"]
}

if movie_id in time_slots:
    print("------------------------------------------------------------")
    print("Available Time Slots:", ', '.join(time_slots[movie_id]))
    print("------------------------------------------------------------")
    preferred_time = input("Enter the preferred time (e.g., 02:30 PM) : ")
    if preferred_time not in time_slots[movie_id]:
        print("Time slot not available.")
        exit()

print("--------Tickets Available--------")
print("------------------------------------------------------------\n")

# Display seat layout
print('SEATS\n')
print("____ ____ ____ ____ ")
print("| A1 | | A2 | | A3 | | A4 |")
print("‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾")
print("____ ____ ____ ____ ____ ____ ____ ____ ")
print("| B1 | | B2 | | B3 | | B4 | | B5 | | B6 | | B7 | | B8 |")
print("‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾")
print("____ ____ ____ ____ ____ ____ ____ ____ ")
print("| C1 | | C2 | | C3 | | C4 | | C5 | | C6 | | C7 | | C8 |")
print("‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾")
print("____ ____ ____ ____ ____ ____ ____ ____ ")
print("| D1 | | D2 | | D3 | | D4 | | D5 | | D6 | | D7 | | D8 |")
print("‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾")
print("____ ____ ____ ____ ____ ____ ____ ____ ")
print("| E1 | | E2 | | E3 | | E4 | | E5 | | E6 | | E7 | | E8 |")
print("‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾")
print("____ ____ ____ ____ ____ ____ ____ ____ ")
print("| F1 | | F2 | | F3 | | F4 | | F5 | | F6 | | F7 | | F8 |")
print("‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾")
print("____ ____ ____ ____ ____ ____ ____ ____ ")
print("| G1 | | G2 | | G3 | | G4 | | G5 | | G6 | | G7 | | G8 |")
print("‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾")
print("____ ____ ____ ____ ____ ____ ____ ____ ")
print("| H1 | | H2 | | H3 | | H4 | | H5 | | H6 | | H7 | | H8 |")
print("‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾")
print("____ ____ ____ ____ ____ ____ ____ ____ ")
print("| I1 | | I2 | | I3 | | I4 | | I5 | | I6 | | I7 | | I8 |")
print("‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾ ‾‾‾‾‾‾\n")

# Collect seat numbers
seats_selected = []

num_tickets = int(input("Enter number of tickets required: "))
print('')

for i in range(num_tickets):
    while True:
        seat_no = input(f"Enter seat number for ticket {i+1} (e.g., A1): ").upper()
        if seat_no in seats_selected:
            print("Seat already taken! Please choose another seat.")
        else:
            seats_selected.append(seat_no)
            break

name = input("\nEnter your full name: ")
phone_no = input("Enter your phone number: ")

# Ticket types and prices
print("\nTicket types:\n1. Adult: Rs.200\n2. Child: Rs.120\n3. Senior Citizen: Rs.100")
ticket_type = input("Select ticket type (Adult/Child/Senior Citizen): ").lower()

ticket_prices = {
    'adult': 200,
    'child': 120,
    'senior citizen': 100
}

if ticket_type not in ticket_prices:
    print("Invalid ticket type selected. Defaulting to Adult.")
    ticket_type = 'adult'

price_per_ticket = ticket_prices[ticket_type]
total_amount = price_per_ticket * num_tickets

print(f"\nTotal amount = Rs. {total_amount}")

# Snacks order
while True:
    snacks_order = input("Would you like to order any snacks? (Yes/No): ").lower()
    if snacks_order == 'yes':
        snacks = input("Enter snacks (comma separated): ")
        break
    elif snacks_order == 'no':
        snacks = "No snacks"
        break
    else:
        print("Please enter 'Yes' or 'No'.")

print("\n------------------------------------------------------------")
print(f"Booking Summary for {name}")
print("------------------------------------------------------------")
print(f"Movie: {movie_name}")
print(f"Date: {movie_date}")
print(f"Time: {preferred_time}")
print(f"Seats: {', '.join(seats_selected)}")
print(f"Tickets: {num_tickets} ({ticket_type.capitalize()})")
print(f"Total Amount: Rs. {total_amount}")
print(f"Snacks: {snacks}")
print(f"Phone Number: {phone_no}")
print("------------------------------------------------------------")

# Insert booking into database using parameterized query
query = """INSERT INTO movie 
(movie_id, movie_name, movie_date, preferred_time, seats, customer_name, phone_no, no_of_tickets, ticket_type, total_amount, snacks)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

values = (movie_id, movie_name, movie_date, preferred_time, ', '.join(seats_selected), name, phone_no, num_tickets, ticket_type, total_amount, snacks)

try:
    cursor.execute(query, values)
    conn.commit()
    print("\nBooking successful! Enjoy your movie.\n")
except Exception as e:
    print(f"An error occurred while saving your booking: {e}")

cursor.close()
conn.close()
