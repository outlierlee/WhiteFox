
```cpp
#include<iostream>
using namespace std;

int main() {
    int i = 0;
    float a = 1.23456, b = -123.456;
    double e = 0.123456789e20, f = 0.123456789e-20;
    
    do{
        ++i;
        a += 1.23456;
        b -= 0.1;
    } while(i < 10);
    
    if(a > b)
        cout << a << "\n";
    else 
        cout << b << "\n";
    
    if(e > f)
        cout << e << "\n";
    else 
        cout << f << "\n";
    
    return 0;
}
```

The C++ program starts above and it ends the exact same way as the C program. Use whichever syntax you feel is easier to read and understand. Or you can make modifications to the C++ program as well. The constraints are minimal because the program does not contain a ton of complex operations with structures, so we can't make it do more complicated things. The `main` function can work with any variables, as long as they're assigned some value before being used in the loop or `if` statements.