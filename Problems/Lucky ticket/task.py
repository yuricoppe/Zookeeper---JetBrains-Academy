# Save the input in this variable
ticket = input()
ticketNumbers = list(ticket)

# Add up the digits for each half
half1 = int(ticketNumbers[0]) + int(ticketNumbers[1]) + int(ticketNumbers[2])
half2 = int(ticketNumbers[3]) + int(ticketNumbers[4]) + int(ticketNumbers[5])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")