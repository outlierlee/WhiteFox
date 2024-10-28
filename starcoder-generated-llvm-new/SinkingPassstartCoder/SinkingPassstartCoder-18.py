
```c
#include <stdio.h>

int main() {
    int a = 15, b = 12, c = 41; // Declare and initialize variables
    int d, e; // Declare more variables

    if (a % 2) { // Conditional block
        d = a + b; // Perform an operation
    } else {
        d = a - b; // Perform a different operation
    }

    if (a > 10) { // An additional conditional block
        e = d * c; // Do an operation with the result
    } else {
        e = d / a; // Another operation with the result
    }

    printf("%d\n", e); // Use the result

    return 0;
}
```

# C Code ends