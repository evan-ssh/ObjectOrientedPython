from rectangle import Rectangle
while True:
    print("Rectangle Calculator")
    height = int(input("Height:"))
    width = int(input("Width:"))
    r = Rectangle(height,width)
    print(f"Perimeter: {r.calculate_perimeter()}")
    print(f"Area: {r.calculate_area()}")
    r.display_rectangle()
    command = input("Calculate another rectangle (y/n):").lower().strip()
    if command != "y":
        break