def calculate_tip_amount(bill, tip_percent, people=1):
    if people <= 0:
        people = 1
    tip = bill * (tip_percent / 100)
    total = bill + tip
    per_person = total / people
    return {
        "bill": round(bill, 2),
        "tip": round(tip, 2),
        "total": round(total, 2),
        "per_person": round(per_person, 2)
    }

if __name__ == "__main__":
    try:
        bill = float(input("Enter the bill amount: R"))
        tip_percent = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
        people = int(input("Split between how many people? "))
    except ValueError:
        print("Please enter valid numbers.")
    else:
        result = calculate_tip_amount(bill, tip_percent, people)
        print(f"\nBill amount: R{result['bill']:.2f}")
        print(f"Tip:R{result['tip']:.2f}")
        print(f"Total amount: R{result['total']:.2f}")
        if people > 1:
            print(f"Each person pays: R{result['per_person']:.2f}")