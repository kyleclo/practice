<!-- 
-->
## Global variables

#### Static, Extern, and Linkage
* Most variables have zero linkage, meaning they can only be accessed within their respective scope

* *Static* variables have internal linkage, meaning they can be used anywhere within the same file
    + Static variables can't be accessed in other files even if we forward declare with *extern* keyword 
    + Static functions can't be accessed in other files even if we include function prototypes with a header file

* *Extern* variables have external linkage, meaning they can be used in other files as well
    + Global variables can have external linkage if forward declared with the *extern* keyword above the *main* function.
    + Functions have external linkage by default.  We gain access to functions defined in other files by including header files.
```{c++}
// global.cpp
int g_x(5);
static int g_y(3);

// main.cpp
extern int g_x;     // forward declaration using extern keyword grants access to g_x defined in global.cpp
extern int g_y;     // fails because g_y is static in global.cpp

int main(){

    std::cout << "g_x defined in global.cpp has value: " << g_x << std::endl;      // prints 5
    std::cout << "g_y defined in global.cpp has value: " << g_y << std::endl;      // compile error because can't find g_y
    
    return 0;
}
```

#### Constant
- Only allow constant (read-only) global variables
- Use namespaces
- Define variables in a *.cpp* file made available via *extern* keyword in forward declarations in a header file
```{c++}
// constants.cpp
namespace Constants{                                // initialize global variables in .cpp file
    extern const double pi(3.14159);
    extern const double gravity(9.2);
}

// constants.h
#ifndef CONSTANTS_H
#define CONSTANTS_H

namespace Constants{                                // forward declarations with extern in .h file
    extern const double pi;
    extern const double gravity;
}

#endif

// main.cpp
#include "constants.h"                              // including .h file gives access to global variables
...
double area = Constants::pi * pow(radius, 2);       // remember to access namespace using ::
```

<hr>










<!-- 
-->
## Switch statements

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
<hr>





<!-- 
-->
## Do-while loops

#### Usage
- Use do-while loops over while loops when you want the loop to execute at least once
```{c++}
int choice;     // declared outside *do* block because need for *while* conditional
do{
    std::cout << "Guess a number between 1 and 10:" << std::endl;
    std::cin >> choice;
}
while(choice < 1 || choice > 10){
    std::cout << "That wasn't between 1 and 10. Try again." << std::endl;
}
```
<hr>





<!-- 
-->
## For loops

#### Comma operator
- Comma operators are typically only ever used in for-loops
```{c++}
for(int i = 0, j = 9; i < 0; i++, j--)
    std::cout << i << " " << j << std::endl;
```

#### Scope of loop iterators
- In newer C++ versions, iterator variables defined in *for()* are destroyed at the end of the loop

#### Return, break, and continue
- *Return* exits the function, *break* exits the loop, and *continue* skips to next iteration

<hr>




<!-- 
-->
## std::cin and extraction operator

#### How does extraction operator >> work?
* If buffer contains no data, prompt user for input.  When user hits Enter, reads everything (including newline character '\n') and places inside *std::cin* buffer 
* If buffer contains data, extract
    + ignore whitespace characters (e.g. spaces, tabs, '\n')
    + as much data as possible into the varaible
    + anything leftover is left in the buffer

#### Types of input error

- Extraction succeed but meaningless
```{c++}
while(1){
    std::cout << "Input your height: " << std::endl;
    int height;
    std::cin >> height;
    
    if(height > 0){
       std::cout << "Your height is " << height << std::endl;
       break;
    }
    else
        std::cout << "You can't have negative height. Try again." << std::endl;
}
```
```
>> Input your height: -5
>> You can't have negative height. Try again.
>> Input your height: 5
>> Your height is 5
```

- Extraction succeed but followed by additional junk
```{c++}
const int maxInputLength = 32767;

std::cout << "Input your height: " << std::endl;
int height;
std::cin >> height;

std::cin.ignore(maxInputLength, '\n');      // clears up to maxInputLength chars from buffer until first '\n' removed

std::cout << "Your height is " << height << std::endl;
```
```
>> Input your height: 5asdf
>> Your height is 5
...
>> Input your height: 5\nasdf
>> Your height is 5
```

- Extraction fails
```{c++}
while(1){
    const int maxInputLength = 32767;

    std::cout << "Input your height: " << std::endl;
    int height;
    std::cin >> height;
    
    if(std::cin.fail()){
        std::cout << "Please input an integer. Try again." << std::endl;
        std::cin.clear();                           // reset to get cin out of failure mode
        std::cin.ignore(maxInputLength, '\n');      // clear everything in buffer
    }
    else{
        std::cout << "Your height is " << height << std::endl;
        break;
    }
}
```
```
>>> Input your height: asdf
>>> Please input an integer. Try again.
>>> Input your height: 5
>>> Your height is 5
```


<hr>








<!-- 
-->
## Pointers
* When to use pointers:
    + dynamically allocate memory
    + pass large data to functions without copying
    + pass function to another function
    + achieve polymorphism through inheritance
    + data structures (e.g. linked lists, trees)

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
int *intPtr(NULL);      // works but bad
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
<hr>






<!-- 
-->
## Arrays

#### Passing to functions
- Make explicit that arrays decay to pointers when passed as function parameters; this causes certain operations (e.g. *sizeof()*) to perform strangely

```{c++}
void PrintSize(int array[]);    // no
void PrintSize(int *array);     // yes
```

#### Dynamically-allocated arrays

- If need to resize arrays, use std::vector rather than attempting to work with dynamically-allocated arrays

<hr>






<!-- 
-->
## Strings

- Use std::string rather than C-style strings (arrays of chars)


