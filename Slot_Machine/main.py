import random

MAX_LINES = 3
MAX_BET = 4000
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            broke_loop = False
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                broke_loop = True
                break
        if(broke_loop == False):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
     
    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)
    
    columns = []
    # loop through cols parameter
    for _ in range(cols):
        # make a empty list
        column = []
        # make a copy of all_symbols
        current_symbols = all_symbols[:]
        # loop through the rows
        for _ in range(rows):
            # choose a random value out of all the symbols
            value = random.choice(all_symbols)
            # remove the chosen value
            current_symbols.remove(value)
            # add the value to the current column
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    # [[1,2,3],[4,5,6][7,8,9]]
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(f"{column[row]}")


def deposit():
    while True:
        amount = input("How much would like to deposit?> $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break;
            else:
                print("Amount must be greater than 0\n")
        else:
            print("Please enter a number\n")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"How many lines would you like to bet on? (1 - {MAX_LINES})?")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break;
            else:
                print("Enter a valid number of lines\n")
        else:
            print("Please enter a number\n")
    
    return lines

def get_bet():
    while True:
        amount = input(f"How much would like to bet on each line (${MIN_BET} - ${MAX_BET})?> $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break;
            else:
                print(f"Amount must be greater than between ${MIN_BET} and ${MAX_BET}\n")
        else:
            print("Please enter a number\n")
    
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You cannot bet that much, your balance is {balance}\n")
        else:
            break;
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    print(balance, lines)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}\n")
        answer = input("Press enter to spin (q to quit)")
        if answer == 'q':
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


# Driver code
main()