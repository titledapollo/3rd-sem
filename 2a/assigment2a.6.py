choice = input("Choose area calculation method (base_height / heron): ").strip().lower()

match choice:
    case "base_height":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = 0.5 * base * height
        print(f"Area of triangle using base and height: {area}")

    case "heron":
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        s = (a + b + c) / 2  
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"Area of triangle using Heron's formula: {area}")

    case _:
        print("Invalid choice")


