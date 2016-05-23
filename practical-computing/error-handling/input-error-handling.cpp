#include <iostream>

const int kMaxInputLength(32767);

double GetDouble();
double GetOperator();
void RunCalculator(double x, char op, double y);

int main(){

    double x = GetDouble();
    char op = GetOperator();
    double y = GetDouble();

    RunCalculator(x, op, y);

    return 0;
}


double GetDouble(){

    while(true){

        std::cout << "Enter a double value: ";
        double x;
        std::cin >> x;

        // Check for failed double extraction (e.g. inputting "asdf" or "5asdf" or "\n")
        if(std::cin.fail()){
            std::cin.clear();                           // reset cin
            std::cin.ignore(kMaxInputLength, '\n');     // flush until newline
            std::cout << "That was invalid. Try again. " << std::endl;
        }

        else{
            // Flush anything after successful extraction (e.g. inputting "5 asdf" or "5\n asdf")
            std::cin.ignore(kMaxInputLength, '\n');

            return x;
        }
    }
}


double GetOperator(){

 while(true){

        std::cout << "Enter one of the following: +, -, *, or /: ";
        char op;
        std::cin >> op;

        // Char extraction always successful.  Flush after.
        std::cin.ignore(kMaxInputLength, '\n');

        if(op == '+' || op == '-' || op == '*' || op == '/')
            return op;
        else
            std::cout << "That was invalid. Try again. " << std::endl;
    }
}

void RunCalculator(double x, char op, double y){

    switch(op){
        case '+':
            std::cout << x << " + " << y << " = " << x + y << std::endl;
            break;
        case '-':
            std::cout << x << " - " << y << " = " << x - y << std::endl;
            break;
        case '*':
            std::cout << x << " * " << y << " = " << x * y << std::endl;
            break;
        case '/':
            std::cout << x << " / " << y << " = " << x / y << std::endl;
            break;
    }
}
