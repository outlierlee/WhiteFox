
```c
#include <stdio.h>

int main() {
    unsigned int a = 10; // Declare and initialize a variable
    unsigned int b = (1 << 31); // Declare and initialize another variable
    unsigned int c = 2; // Declare a variable to store the result

    if (a > 5) { // Conditional block
        short x=10, y=5; 
        float z=12.5; 
        c = a + b; // Perform an operation 
    } else { 
        c = a - b; // Perform a different operation
    } 

    if (c > 10 && c < 15) {
        c += 5;
    } else if (c > 20) {
        c -= 5;
    }

    printf("%d\n", c); // Use the result

    return 0;
}
```
