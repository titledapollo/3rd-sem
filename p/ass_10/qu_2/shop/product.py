def add_product():
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter available quantity: "))
    print("\n✅ Product added successfully!")
    return {"id": product_id, "name": name, "price": price, "quantity": quantity}
