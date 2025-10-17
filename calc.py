def calculate_tip():
    try:
        bill = float(input("Enter the bill amount: R"))
        tip_percent = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
        people = int(input("Split between how many people? "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    tip = bill * (tip_percent / 100)
    total = bill + tip
    per_person = total / people if people > 0 else total

    print(f"\nBill amount: R{bill:.2f}")
    print(f"Tip: R{tip:.2f}")
    print(f"Total amount: R{total:.2f}")
    if people > 1:
        print(f"Each person pays: R{per_person:.2f}")

if __name__ == "__main__":
    calculate_tip()