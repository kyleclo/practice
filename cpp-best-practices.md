## Switch

#### Chaining if-else statements
- Switch statements are typically more efficient than if-else chains

#### Variable declaration / initialization / assignment
- Use blocks when declaring variables in the cases
```{c++}
switch(x){
    case 1:
        int y;          // OK because declaration allowed
        y = 5;          // OK because assignment allowed
        break;          // avoid fall-through
    case 2:
        y = 10;         // OK because y declared above
        break;
    case 3;
        int z = 15;     // compile error: initialization not allowed
        break;
    case 4:
    {
        int w = 15;     // OK because within block
        break;
    }
}
```


## Pointers
- When to use pointers:
    - dynamically allocate memory
    - pass large data to functions without copying
    - pass function to another function
    - achieve polymorphism through inheritance
    - data structures (e.g. linked lists, trees)

#### Naming
- When declaring pointer variables, put asterisk next to variable name

```{c++}
int *intPtr1, *intPtr2;
```

- When declaring functions returning pointers, put asterisk next to type

```{c++}
int* doSomething();
```

#### Initialization
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

#### Dynamic allocation
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

#### *Const* pointers
- Primarily used in function parameters (e.g. passing arrays) to help ensure function doesn't change passed argument
```{c++}
```


## Arrays

#### Passing to functions
- Make explicit that arrays decay to pointers when passed as function parameters; this causes certain operations (e.g. *sizeof()*) to perform strangely

```{c++}
void PrintSize(int array[]);    // no
void PrintSize(int *array);     // yes
```

#### Dynamically-allocated arrays

- If need to resize arrays, use std::vector rather than attempting to work with dynamically-allocated arrays



## Strings

- Use std::string rather than C-style strings (arrays of chars)


