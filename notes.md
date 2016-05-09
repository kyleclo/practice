<!-- 
-->
## What are Static Local variables

* Local variables (ones defined in a block) by default have automatic duration, meaning they are created / destroyed when the block is entered / exited.

* *Static* variables have fixed duration, meaning they are initialized once and persist even after their scope has exited.
```{c++}
void incrementAndPrint(){
    static int s_x(0);
    s_x++;
    std::cout << s_x << std::endl;
}                           // lose access to x when scope exits (block ends), but x retains value

int main(){
    incrementAndPrint();    // s_x = 1
    incrementAndPrint();    // s_x = 2
    
    return 0;
}
```
<hr>




<!-- 
-->
## Global variables

#### What are Static Global variables
* Most variables have zero linkage, meaning they can only be accessed within their respective scope

* *Static* global variables have internal linkage, meaning they can be used anywhere within the same file
    + Static global variables can't be accessed in other files even if we forward declare with *extern* keyword 
    + Static functions can't be accessed in other files even if we include function prototypes with a header file

* *Extern* variables have external linkage, meaning they can be used in other files as well
    + Non-static Global variables can have external linkage if forward declared with the *extern* keyword above the *main* function.
    + Non-static functions have external linkage by default.  We gain access to them by including header files.
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

<hr>








<!-- 
-->
## For loops

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








<!-- 
-->
## Enumeration

#### Memory
* No memory is allocated when an *enum* is defined
* Memory is only allocated when a variable of that type is declared

