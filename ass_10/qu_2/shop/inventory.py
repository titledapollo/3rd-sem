def show_inventory(products):
    print("\n📦 INVENTORY DETAILS:")
    if not products:
        print("No products available.")
        return
    for p in products:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ₹{p['price']} | Stock: {p['quantity']}")
