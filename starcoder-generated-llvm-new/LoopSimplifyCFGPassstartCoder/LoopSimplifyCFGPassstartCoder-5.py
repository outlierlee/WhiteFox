
```c
#include <stdio.h>

int main() {
    unsigned int x = 10; // declare and initialize x
    unsigned int y = 3; // declare and initialize y

    // A loop with a condition that can be constant-folded
    while (x > 5) {
        // Perform some operations
        x = x - y; // x is updated with an operation involving y
    }

    return x; // return the result
}
```

