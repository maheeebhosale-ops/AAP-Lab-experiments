# Experiment 3: Configurable Payment Processing System using Strategy Pattern

from abc import ABC, abstractmethod


# ---------- Strategy Interface ----------
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# ---------- Concrete Strategies ----------
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, holder_name):
        self.card_number = card_number
        self.holder_name = holder_name

    def pay(self, amount):
        masked = "**** **** **** " + self.card_number[-4:]
        print(f"Paid Rs. {amount} using Credit Card {masked} ({self.holder_name})")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid Rs. {amount} using PayPal account {self.email}")


class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Paid Rs. {amount} using Bitcoin wallet {self.wallet_address}")


class UPIPayment(PaymentStrategy):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paid Rs. {amount} using UPI ID {self.upi_id}")


# ---------- Context ----------
class PaymentProcessor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy
        print(f"Payment method switched to: {strategy.__class__.__name__}")

    def process_payment(self, amount):
        if self.strategy is None:
            print("No payment method selected!")
            return
        self.strategy.pay(amount)


# ---------- Main ----------
def main():
    print("=== PAYMENT PROCESSING SYSTEM (Strategy Pattern) ===\n")

    processor = PaymentProcessor()

    processor.set_strategy(CreditCardPayment("4532789012345678", "Neil Hole"))
    processor.process_payment(2500)

    print()
    processor.set_strategy(PayPalPayment("neil.hole@example.com"))
    processor.process_payment(1200)

    print()
    processor.set_strategy(BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7"))
    processor.process_payment(7800)

    print()
    processor.set_strategy(UPIPayment("neil@okaxis"))
    processor.process_payment(499)

    print("\n--- Runtime Selection by User ---")
    options = {
        "1": CreditCardPayment("9876543210001234", "Neil Hole"),
        "2": PayPalPayment("neil.hole@example.com"),
        "3": BitcoinPayment("3FZbgi29cpjq2GjdwV8eyHuJJnkL"),
        "4": UPIPayment("neil@okhdfc"),
    }

    print("1. Credit Card  2. PayPal  3. Bitcoin  4. UPI")
    choice = input("Choose payment method (1-4): ").strip()
    amount = float(input("Enter amount: "))

    if choice in options:
        processor.set_strategy(options[choice])
        processor.process_payment(amount)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
