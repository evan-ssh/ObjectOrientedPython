from shapes import Rectangle,Square
def main():
    print("Rectangle And Square Calculator")
    while True:
        CalcShape = input("Rectangle or Square?: ").lower()
        if CalcShape[0] == "r":
            width = int(input("Width: "))
            height = int(input("Height: "))
            rect = Rectangle(height, width)
            print(f"Perimeter: {rect.calcPerimeter()}")
            print(f"Area: {rect.calcArea()}")
            print(rect)
            go_again = input("Would you like to go again? (y/n): ")
            if go_again.lower() != "y":
                print("Goodbye!")
                break
        elif CalcShape[0] == "s":
            length = int(input("Length: "))
            square = Square(length)
            print(f"Perimeter: {square.calcPerimeter()}")
            print(f"Area: {square.calcArea()}")
            print(square)
            go_again = input("Continue? (y/n): ")
            if go_again.lower() != "y":
                print("Goodbye!")
                break
if __name__ == "__main__":
    main()