# Factory

We use the Factory pattern when we want to instantiate objects from different classes that are grouped under a common superclass or interface.  This could look something like:

```python
my_triangle = Triangle()
my_circle = Circle()
my_square = Square()
...
```

where `Triangle`, `Circle`, and `Square` all implement the `Shape` abstract base class.

This is fine, but we can run into certain problems.

### Problem 1:  Class needs to be chosen at run time

For example, what if we want to generate shapes randomly, or shapes are chosen by the user when prompted?  Well, we could expand the code above to look like:

```python
#  choose ID of shape via random number generator or input
if id == 1:
    my_shape = Triangle()
elif id == 2:
    my_shape = Circle()
elif id == 3:
    my_shape = Square()
...
```

The way to do this would be to have a centralized location with all the constructors and use a Random Number Generator to select the id of the desired shape to instantiate.





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


