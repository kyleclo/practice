# Factory

We use the Factory pattern when we want to instantiate objects from different classes that are grouped under a common superclass or interface.

### Usual approach

Instantiating a bunch of objects could look like:

```python
my_triangle = Triangle()
my_circle = Circle()
my_square = Square()
...
```

where `Triangle`, `Circle`, and `Square` all implement the `Shape` abstract base class.

This is fine for simple situations, but what if the Class needs to be chosen at run-time?  For example, what if we want to generate shapes randomly, or shapes are chosen by the user when prompted?

### Alternative approach

To handle this, we could modify the code above to look like:

```python
id = ... #choose ID via random number generator or user input

if id == 1:
    my_shape = Triangle()
elif id == 2:
    my_shape = Circle()
elif id == 3:
    my_shape = Square()
...
```

If we want to instantiate many objects (e.g. generate 10 random shapes) then we'd want to wrap this entire if-else chain into a single, reusable command.  That is what a **Factory** provides!

### Using a Factory

```python
class ShapeFactory:
    def createShape(type):
        if type == 'triangle':
            return Triangle()
        elif type == 'circle':
            return Circle()
        elif type == 'square':
            return Square()
        else:
            print 'That's not a shape!'
            return None
```

Now, I can create many new `Shape` objects like so:

```python
my_shape_factory = ShapeFactory()

shape_names = ... #choose names via random number generator or user input

my_shapes = list()
for name in shape_names:
    my_shapes.append(my_shape_factory.createShape(name))
```

And thus, the Factory centralizes all the code for instantiating these similar objects and makes it reusable.

#### Useful for statistical models

Factories become especially useful if there is large overhead in instantiating objects.  For example, suppose you have many statistical models to instantiate.  Then, we can start with an abstract base class:

```python
class Classifier:
    def __init__(self):
        self.params = None
        
    def train(self, train_x, train_y):
        raise NotImplementedError
    
    def predict(self, test_x):
        raise NotImplementedError
```

and define subclasses like `LogisticRegression` and `DecisionTree`.



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


