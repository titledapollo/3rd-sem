from shop import product, billing, inventory

def main():
    products = []

    while True:
        print("\n===== SHOP MENU =====")
        print("1. Add Product")
        print("2. Show Inventory")
        print("3. Generate Bill")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            prod = product.add_product()
            products.append(prod)
        elif choice == '2':
            inventory.show_inventory(products)
        elif choice == '3':
            billing.generate_bill(products)
        elif choice == '4':
            print("👋 Thank you! Visit again.")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
