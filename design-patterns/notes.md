## Factory

### Problem

Suppose we have an application that requires the **instantiation** of `Shape` objects with `draw` methods:

```python
def main():
    my_shapes = []
    my_shapes.append(Circle())
    my_shapes.append(Circle())
    my_shapes.append(Square())
    my_shapes.append(Square())

    for shape in my_shapes:
        shape.draw()
```

### Approach 1

We can use an **interface** (see **abstract base class** for Python) that requires every `Shape` to implement a `draw` method.

```python
class Shape:
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        print 'Drawing a circle.'

class Square(Shape):
    def draw(self):
        print 'Drawing a square.'
```

The problem with this approach comes when others want to add their own shapes.

### Approach 2

We can define a **factory class** whose purpose is to instantiate `Shape` objects.
