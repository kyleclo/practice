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




# Iterator
<font color = 'red'> Why do we use this at all? </font>

I want the ability to iterate over elements of something in a sequential manner without knowing its representation.

First, create two interfaces.  The `Container` will contain the elements to iterate over.  The `Iterator` will be an object that fetches the next element.

```python
class Container:
    def get_iterator():
        raise NotImplementedError
        
class Iterator:
    def get_next():
        raise NotImplementedError
```

Second, implement the `Container` interface.  Since the `Container` has a method that returns an `Iterator`, the interface forces us to provide an implementation of the `Iterator` interface.

```python
class MyIterableThing(Container):

    self.iterable = [1, 2, 3, 4, 5]
    
    def get_iterator():
        return _IteratorForMyIterableThing(self.iterable)

class _IteratorForMyIterableThing(Iterator):

        def __init__(self, iterable):
            self.index = 0
            self.iterable = iterable
    
        def get_next():
            if self.index < len(self.iterable):
                next = self.iterable[self.index]
                self.index += 1
                return next
            return None
```


