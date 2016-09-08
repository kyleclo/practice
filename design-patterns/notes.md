# Factory Method

We use this design pattern when we want to **instantiate objects** from different classes that are grouped under a common superclass/interface.

### Usual approach

Instantiating a bunch of objects could look like:

```python
my_triangle = Triangle()
my_circle = Circle()
my_square = Square()
```
where `Triangle`, `Circle`, and `Square` all implement the `Shape` abstract base class.

### Factories

Alternatively, we can define a `Factory` class that provides a `create()` method for instantiating new `Shape` objects:

```python
class ShapeFactory:
    def create(self, name):
        if name == 'triangle':
            return Triangle()
        elif name == 'circle':
            return Circle()
        elif name == 'square':
            return Square()
        else:
            print 'That's not a shape!'
            return None
```

For example, the `main` script using this Factory could look like:

```python
my_shape_factory = ShapeFactory()

while True:
    name = ... #some way of choosing a shape (e.g. RNG or user input)
    my_shape = my_shape_factory.create(name)
    my_shape.display()
```

### Factory Method

The Factory Method pattern is very similar to using a regular Factory, but defines the `create()` function as a **static method in the superclass** rather than a method in a separate Factory class.  

For example, the `main` script using this static method would include the expression:

```python
my_shape = Shape.create(name)
```


### Reasons to use the Factory Method pattern

- Classes need to be **chosen at run-time** because they depend on some **external source** (e.g. user input, random number generator, read file, etc.)

- We want to **centralize** the management of all instantiated objects (e.g. keep track of how many there are, parameters depend on what's been previously instantiated, share a common resource, etc.)

<hr>



# Iterator
Suppose I have a `Container`, which is some data structure containing multiple elements that can be iterated over.  I want the ability to iterate over these elements.

Well, we could just use an array if elements are primitives:

```python
def main():
    my_container = [1, 2, 3, 4, 5]
    for x in my_container:
        print x
```

and define our own iterator if we have something more complicated like a `Tree` or `LinkedList`:

```python
def main():
    my_container = Tree()
    
```


### Approach 1

I could 




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


