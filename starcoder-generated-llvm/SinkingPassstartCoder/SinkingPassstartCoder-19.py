
```c
#include <stdio.h>

int main() {
    float a = 0.1, b = 1.0, c, d, e;    // Declare and initialize variables
    int f = 3, g = 10;  // Declare and initialize more variables
    
    // Declare and initialize a variable using a selection statement
    if (f > g) {
        c = b / a;
    } else {
        c = b * a;
    }
    
    d = 1.0 * f + a;     // An arithmetic operation involving a common factor
    e = c + d;           // Another operation involving a common factor
    
    printf("%f\n", e);    // Print the result
    
    return 0;
}
```
