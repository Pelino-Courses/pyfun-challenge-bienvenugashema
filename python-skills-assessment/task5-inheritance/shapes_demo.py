from shapes import Circle, Rectangle, Triangle


def main():
    """
    Entry point for user interaction. Prompts the user to choose a shape,
    input its dimensions, and displays the area.
    """
    options = {
        "1": Circle,
        "2": Rectangle,
        "3": Triangle
    }

    print("Choose a shape to calculate area:")
    print("1. Circle\n2. Rectangle\n3. Triangle")

    try:
        choice = input("Enter option (1-3): ").strip()
        shape_class = options.get(choice)

        if shape_class == Circle:
            radius = float(input("Enter radius: "))
            shape = Circle(radius)

        elif shape_class == Rectangle:
            height = float(input("Enter height: "))
            width = float(input("Enter width: "))
            shape = Rectangle(height, width)

        elif shape_class == Triangle:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            shape = Triangle(base, height)

        else:
            print("Invalid option selected.")
            return

        print(f"\n{shape}")
        print(f"Area: {shape.area():.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except KeyboardInterrupt:
        print("\nProgram exited.")

if __name__ == "__main__":
    main()
