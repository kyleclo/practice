# Factory

We use the Factory pattern when we want to instantiate objects from different classes that are grouped under a common superclass or interface.

### Usual approach

Instantiating a bunch of objects could look like:

```python
my_triangle = Triangle()
my_circle = Circle()
my_square = Square()
```

where `Triangle`, `Circle`, and `Square` all implement the `Shape` abstract base class.

This is fine in many situations, but what if the classes need to be chosen at run-time?  For example:
- Shapes generated according to a random number generator
- Shapes chosen depend on some input (e.g. user prompt or a read file)

### Using a Factory

```python
class ShapeFactory:
    def create(name):
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

Now, I can create many new `Shape` objects through my instantiated `Factory`.  For example, the `main` function could look like this:

```python
my_shape_factory = ShapeFactory()

my_shapes = list()
while not stopping_condition:
    name = ... #some method of choosing a shape (e.g. RNG or user input)
    my_shapes.append(my_shape_factory.create(name))
...
```


<!-- 
#### Useful for statistics

Factories become especially useful if there is large overhead in instantiating objects. 

Suppose you have many statistical models to instantiate that all operate on the same dataset.  Then, we can start with an abstract base class:

```python
class Classifier:
    def __init__(self, df):
        self.data = df
        self.train_x, self.train_y, self.test_x, self.test_y = ... # random splitting
        self.params = None
    
    def train(self):
        raise NotImplementedError
    
    def predict(self):
        raise NotImplementedError
```

and define subclasses like `LogisticRegression` and `ClassificationTree`. 

#### Unit testing

-->

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


