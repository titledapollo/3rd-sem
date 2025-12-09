def generate_bill(products):
    total = 0
    while True:
        product_id = input("\nEnter product ID to buy (or 'done' to finish): ")
        if product_id.lower() == "done":
            break

        for p in products:
            if p["id"] == product_id:
                qty = int(input("Enter quantity: "))
                if qty <= p["quantity"]:
                    cost = p["price"] * qty
                    total += cost
                    p["quantity"] -= qty
                    print(f"✅ Added {qty} x {p['name']} = ₹{cost}")
                else:
                    print("❌ Not enough stock!")
                break
        else:
            print("❌ Product not found!")

    print(f"\n🧾 Total Bill Amount: ₹{total}")
    print("💳 Thank you for shopping!")
