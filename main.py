import json

class BillManager:

    def __init__(self):
        with open("bills.json", "r") as f:
            self.bills = json.load(f)

    def add_bill(self, company: str, bill_type: str, amount: float, date_paid: str) -> None:
        self.bills["bills"].append({
            "company": company,
            "bill_type": bill_type,
            "amount": amount,
            "date_paid": date_paid,
        })

    def save_bills(self):
        with open("bills.json", "w+") as f:
            json.dump(self.bills, f, indent=4)

        print("Payments recorded.")

def main():
    bill_manager = BillManager()

    while True:
        company = input("Which company is this bill for? ")
        bill_type = input("What type of bill did you pay? ")
        amount = input("How much did you pay? ")
        date_paid = input("When did you pay? ")

        bill_manager.add_bill(company, bill_type, amount, date_paid)

        is_another_payment = input("Would you like to add another payment? ")
        if is_another_payment == "No":
            print("No more payments.") 
            bill_manager.save_bills()
            break

if __name__ == "__main__":
    main()

