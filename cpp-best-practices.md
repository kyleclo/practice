#### Pointers
- When to use pointers:
    - dynamically allocate memory
    - pass large data to functions without copying
    - pass function to another function
    - achieve polymorphism through inheritance
    - data structures (e.g. linked lists, trees)

- When declaring pointer variables, put asterisk next to variable name

```{c++}
int *intPtr1, *intPtr2;
```

- When declaring functions returning pointers, put asterisk next to type

```{c++}
int* doSomething();
```

- In C++11, initialize null pointers with *nullptr* which can be useful for null pointer checking

```{c++}
int *intPtr(nullptr);
if(intPtr) std::cout << "Pointer is pointing to an int variable" << std::endl;
else std::cout << "Pointer is a null pointer" << std::endl;
```

- Avoid using NULL because it's a preprocessor macro that's not technically part of C++

```{c++}
int *intPtr(NULL);
```

- Avoid dangling pointers after deleting memory by setting them to null
```{c++}
int *intPtr = new int;
delete intPtr;
intPtr = nullptr;
```

- Check whether *new* successfully allocated memory prior to attempting to dereference
```{c++}
int *intPtr = new (std::nothrow) int;       // set to nullptr if integer allocation failed
if(!intPtr){
    std::cout << "Could not allocate memory" << std::endl;
    exit(1);
}
```

- Avoid memory leak by (1) deleting memory allocated via *new*, and (2) avoiding overwriting pointers containing addresses to *new*-allocated memory
```{c++}
int x = 5;
int *intPtr = new int;  // intPtr contains address to memory allocated for an int
intPtr = &x;            // overwrites address with address of x; now no way of accessing above-allocated memory
```



#### Arrays
- Make explicit that arrays decay to pointers when passed as function parameters; this causes certain operations (e.g. *sizeof()*) to perform strangely

```{c++}
void PrintSize(int array[]);
void PrintSize(int *array);
```

#### Strings
- Use string class from <string> rather than C-style strings (arrays of chars)

```{c++}

```
