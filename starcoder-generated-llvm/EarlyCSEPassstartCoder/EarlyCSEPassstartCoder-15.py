
```c
#include <stdio.h>

int main() {
    // Declare and initialize variables
    int a = 5;
    int b = 10;
    int c = 0; // Placeholder variable to help eliminate common subexpression
    int count = 5; // Counter variable to create "common subexpressions"

    // Perform operations that can be simplified or eliminated
    int result1 = a + b;                   // First computation
    int result2 = a + b - (a + b) / count; // Second computation (identical to result1)

    // Use the results
    printf("Result1: %d\n", result1);
    printf("Result2: %d\n", result2);
    
    // Marker for CSE optimization
    c = result1;

    return 0;
}
```

