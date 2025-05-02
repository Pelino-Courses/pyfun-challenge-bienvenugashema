import math

class Shape:
    """
    Abstract base class for all geometric shapes.
    
    Methods:
        area(): Should be overridden by subclasses to calculate area.
        __str__(): Returns the class name.
        validate_measurement(value, name): Validates numeric input.
    """

    def area(self) -> float:
        """
        Raises NotImplementedError.
        This method must be overridden by subclasses to compute area.
        """
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self) -> str:
        """
        Returns a string representation of the shape class.
        """
        return self.__class__.__name__

    @classmethod
    def validate_measurement(cls, value, name):
        """
        Validates that the input is a positive number.
        
        Args:
            value (int|float): The number to validate.
            name (str): Name of the value, used in error messages.
        
        Raises:
            ValueError: If value is not a positive number.
        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{name} must be a positive number")

class Circle(Shape):
    """
    Circle shape class. Inherits from Shape.

    Attributes:
        radius (float): Radius of the circle.
    """

    def __init__(self, radius: float):
        """
        Initializes a Circle instance with radius validation.
        
        Args:
            radius (float): Radius of the circle.
        """
        self.validate_measurement(radius, "Radius")
        self.radius = float(radius)

    def area(self) -> float:
        """
        Calculates the area of the circle.
        
        Returns:
            float: Area value.
        """
        return math.pi * self.radius ** 2

    def __str__(self):
        """
        Returns a formatted string representation of the circle.
        """
        return f"Circle(radius={self.radius:.2f})"

class Rectangle(Shape):
    """
    Rectangle shape class. Inherits from Shape.

    Attributes:
        height (float): Height of the rectangle.
        width (float): Width of the rectangle.
    """

    def __init__(self, height, width):
        """
        Initializes a Rectangle instance with height and width validation.
        
        Args:
            height (float): Height of the rectangle.
            width (float): Width of the rectangle.
        """
        self.validate_measurement(height, "Height")
        self.validate_measurement(width, "Width")
        self.height = float(height)
        self.width = float(width)

    def area(self) -> float:
        """
        Calculates the area of the rectangle.
        
        Returns:
            float: Area value.
        """
        return self.height * self.width

    def __str__(self):
        """
        Returns a formatted string representation of the rectangle.
        """
        return f"Rectangle(height={self.height}, width={self.width})"

class Triangle(Shape):
    """
    Triangle shape class. Inherits from Shape.

    Attributes:
        base (float): Base of the triangle.
        height (float): Height of the triangle.
    """

    def __init__(self, base, height):
        """
        Initializes a Triangle instance with base and height validation.
        
        Args:
            base (float): Base length of the triangle.
            height (float): Height of the triangle.
        """
        self.validate_measurement(base, "Base")
        self.validate_measurement(height, "Height")
        self.base = float(base)
        self.height = float(height)

    def area(self) -> float:
        """
        Calculates the area of the triangle.
        
        Returns:
            float: Area value.
        """
        return 0.5 * self.base * self.height

    def __str__(self):
        """
        Returns a formatted string representation of the triangle.
        """
        return f"Triangle(base={self.base}, height={self.height})"

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
