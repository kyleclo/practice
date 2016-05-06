<!-- 
-->
## Casts

#### Usage
* Avoid casting at all

* If you must, use C++ *static_cast*
    + checked at compile-time

* Avoid C-style cast since they're not checked by compiler at compile-time, so will allow strange things:
    + removing *const*
    + changing data type without changing underlying representation
```{c++}
int num(5);
int denom(2);

double quotient = double(num) / denom;                  // works, but avoid c-style cast
double quotient = static_cast<double>(num) / denom;     // ok
```






<!--
-->
## Enumeration

#### Naming
* Start enum identifier with capital letter
* Use all caps for enumerator values
* Include the enum identifier as prefix in the enumerator values (unless using *enum class*)
```{c++}
enum Color{
    COLOR_BLACK,
    COLOR_RED,
    COLOR_BLUE
}
```

#### Enum vs Enum Class
* If using C++11, prefer *enum class* over *enum*
    + With *enum*, identifier and enumerator values are all within the same scope, which means we can't prevent strange comparison between variables of different enum types
    + With *enum class*, enumerations become strongly typed and strongly scoped
    
* Also, when using *enum class*, don't need to include identifier as prefix in enumerator values
```{c++}
enum Color{                     // naive enum
    COLOR_RED,
    COLOR_BLUE
};

enum Fruit{
    FRUIT_BANANA,
    FRUIT_APPLE
};

Color color = COLOR_RED;        // Color and COLOR_RED same scope
Fruit fruit = FRUIT_BANANA;

if(color == fruit)              // still executes because RED and BANANA implicit cast to int 0 value
...
```

```{c++}
enum class Color{                   // enum class instead of enum
    RED,
    BLUE
};

enum class Fruit{
    BANANA,
    APPLE
};

Color color = Color::RED;           // can't access RED directly anymore because only exists within scope of Color
Fruit fruit = Fruit::BANANA;        // same with BANANA

if(color == fruit)                  // compiler error here because don't know how to compare across types
...

if(color == Color::RED)             // ok
...

if(static_cast<int>(color) == static_cast<int>(fruit))      // ok
...
```




#### Declare in Header Files
* Can't forward declare enum types because compiler doesn't know how much memory to allocate until a variable of that type is defined
* If an enum is needed in multiple files, define it in a header file and include

#### Uses
* Useful for error reporting within functions
```{c++}
enum class ParseResult{
    SUCCESS = 0,
    ERROR_OPENING_FILE = -1,
    ERROR_READING_FILE = -2,
    ERROR_PARSING_FILE = -3
};

ParseResult ReadFile(){
    if(! OpenFile() )
        return ParseResult::ERROR_OPENING_FILE;
    if(! ReadFile() )
        return ParseResult::ERROR_READING_FILE;
    if(! ParseFile() )
        return ParseResult::ERROR_PARSING_FILE;
    
    return ParseResult::SUCCESS;
}

int main(){
    if(ReadFile() == ParseResult::SUCCESS){
        DoSomething();
    }
}
```

* Useful for defining function options
```{c++}
enum class SortType{
    BACKWARDS,
    FORWARDS
};

void Sort(SortType type){
    if(type == SortType::BACKWARDS)
    ...
```





<!-- 
-->
## Namespaces

#### Avoid using *Using*
+ ... especially in global scope
```{c++}
// bad
using namespace Foo;        // global scope namespaces are dangerous
int main(){
    DoSomething();          // what if there's another DoSomething()?

...

// still bad
int main(){
    using namespace Foo;    // namespace scope limited to block, but can't use Goo::DoSomething() in main()
    DoSomething();

...

// better but awkward
int main(){
    {
        using namespace Foo;
        DoSomething();
    }
    {
        using namespace Goo;
        DoSomething();
    }

...

// safest
int main(){
    Foo::DoSomething();
```

#### Avoid Nesting Namespaces
* C++ namespaces were designed to prevent naming collisions, not implement information hierarchy
```{c++}
namespace Foo{                      // remember namespaces declared in global scope (often in header files)
    namespace Goo{
        void DoSomething(){
            std::cout << "hi" << std::endl;
        }
    }
}

namespace Hoo = Foo::Goo;

int main(){
    Foo::Goo::DoSomething();        // works but...
    Hoo::DoSomething;               // ...why?
```





<!-- 
-->
## Static Local variables

#### Naming
* Static variables typically named with the *s_* prefix

#### Useful as Unique ID generators
```{c++}
int GenerateID(){
    static int s_itemID(0);     // initialized once
    return s_itemID++;          // returns next ID value and increments for next use
}
```

<hr>






<!-- 
-->
## Global variables

#### Keep Constant
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

#### Efficiency
- Switch statements are typically more efficient than if-else chains

#### Use Blocks
- Gets around restrictions regarding variable initialization
- Clears up scope of variables defined within cases
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

#### Return, break, and continue
- *Return* exits the function, *break* exits the loop, and *continue* skips to next iteration

<hr>







<!-- 
-->
## std::cin and extraction operator

#### Dealing with Input Error

- Extraction succeed but meaningless
```{c++}
while(1){
    std::cout << "Input your height: ";
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

std::cout << "Input your height: ";
int height;
std::cin >> height;

std::cin.ignore(maxInputLength, '\n');      // clears up to maxInputLength chars from buffer until first '\n' removed

std::cout << "Your height is " << height << std::endl;
```
```
>> Input your height: 5\nasdf
>> Your height is 5
```

- Extraction fails
```{c++}
while(1){
    const int maxInputLength = 32767;

    std::cout << "Input your height: ";
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

#### Naming
- When declaring pointer variables, put asterisk next to variable name
```{c++}
int *intPtr1, *intPtr2;     // makes sense when declaring multiple pointers in one line
```

- When declaring functions that return pointers, put asterisk next to type
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
int *intPtr(NULL);      // still works but bad
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
- Use in function parameters (e.g. passing arrays) to ensure function doesn't change passed argument
```{c++}
```
<hr>






<!-- 
-->
## Arrays

#### Fixed Arrays
* Array size is optional when Initializing
```{c++}
int array[] = {1,2,3};      // equivalent to int array[3] = {1,2,3};
```

* If possible, use *enum* to create meaningful indices.  Also conveniently uses final enumerator as array size.
```{c++}
// use namespace to maintain proper scope of enumerators (like enum class) without hassle of static_cast<int>
namespace StudentNames{
    enum StudentNames{
        ANNE,           // 0
        BOB,            // 1
        CHARLIE,        // 2
        MAX_STUDENTS    // 3
    };
}

int main(){
    int testScores[StudentNames::MAX_STUDENTS];     // MAX_STUDENTS = 3 is not a variable, so this initialization works
    testScores[StudentNames::ANNE] = 90;
    
    return 0;
}
```

#### Passing to functions
- Make explicit that arrays decay to pointers when passed as function parameters; this causes certain operations (e.g. *sizeof*) to perform strangely

```{c++}
void PrintSize(int array[]);    // no
void PrintSize(int *array);     // yes
```

#### Dynamic Arrays

- If need to resize arrays, use std::vector rather than attempting to work with dynamically-allocated arrays

<hr>






<!-- 
-->
## Strings

#### Usage
* Use std::string rather than C-style strings (arrays of chars)

#### Getting user input

* Use *getline* function instead of *>>* operator
```{c++}
#include <iostream>
#include <string>

int main(){

    std::cout << "Enter your full name: ";
    std::string name;
    std::getline(std::cin, name);       // instead of std::cin >> name;

    std::cout << "Enter your age: ";
    int age;
    std::cin >> age;

    std::cout << name << " is " << age << " years old." << std::endl;

    return 0;
}
```

```
***** Using >> *****
>> Enter your full name: kyle lo
>> Enter your age: kyle is 0 years old.
```

```
***** Using getline *****
>> Enter your full name: kyle lo
>> Enter your age: 18
>> kyle lo is 18 years old.
```





<hr>







<!-- 
-->
