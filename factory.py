# Factory pattern is a software design pattern that provides an interface for creating objects
# but delegates the instantiation logic to its subclasses. it falls under the creational design pattern category
# and promotes loose coupling between the client code and object creation process

# write down a example

class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("drawing a circle")


class Rectangle(Shape):
    def draw(self):
        print("drawing a rectangle")


class Square(Shape):
    def draw(self):
        print("drawing a Square")


class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Invalid shape type")


if __name__ == "__main__":
    # use factory pattern to generate objects
    factory = ShapeFactory()

    circle = factory.create_shape("circle")
    circle.draw()  # Output: Drawing a circle

    rectangle = factory.create_shape("rectangle")
    rectangle.draw()  # Output: Drawing a rectangle

    square = factory.create_shape("square")
    square.draw()  # Output: Drawing a square
