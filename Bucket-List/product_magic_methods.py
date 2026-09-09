# Bucket List Experiment 8: Product with Magic Methods

class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    # combine two products into a cart-like product
    def __add__(self, other):
        if isinstance(other, Product):
            combined_name = f"{self.name} + {other.name}"
            total_price = self.total() + other.total()
            return Product(combined_name, total_price, 1)
        return NotImplemented

    # comparison of prices
    def __lt__(self, other):
        return self.total() < other.total()

    def __gt__(self, other):
        return self.total() > other.total()

    def __eq__(self, other):
        return self.total() == other.total()

    # readable output
    def __str__(self):
        return f"{self.name} | Rs.{self.price} x {self.quantity} = Rs.{self.total()}"

    # developer friendly output
    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"

    def total(self):
        return self.price * self.quantity


def main():
    print("=== PRODUCT WITH MAGIC METHODS ===\n")

    p1 = Product("Laptop", 55000, 1)
    p2 = Product("Mouse", 750, 2)

    print("--- Products ---")
    print(p1)
    print(p2)

    print("\n--- __add__ (combining products) ---")
    combined = p1 + p2
    print(combined)

    print("\n--- __repr__ ---")
    print(repr(p1))
    print(repr(p2))

    print("\n--- Comparing prices ---")
    if p1 > p2:
        print(f"{p1.name} is costlier than {p2.name}")
    elif p1 < p2:
        print(f"{p1.name} is cheaper than {p2.name}")
    else:
        print("Both cost the same")

    print("\n--- User Input ---")
    n1 = input("Enter first product name: ")
    pr1 = float(input("Enter price: "))
    q1 = int(input("Enter quantity: "))

    n2 = input("Enter second product name: ")
    pr2 = float(input("Enter price: "))
    q2 = int(input("Enter quantity: "))

    u1 = Product(n1, pr1, q1)
    u2 = Product(n2, pr2, q2)

    print("\n--- Your Products ---")
    print(u1)
    print(u2)

    print("\nCombined Bill:")
    print(u1 + u2)

    costlier = u1 if u1 > u2 else u2
    print(f"\nCostlier product: {costlier.name} (Rs.{costlier.total()})")


if __name__ == "__main__":
    main()
