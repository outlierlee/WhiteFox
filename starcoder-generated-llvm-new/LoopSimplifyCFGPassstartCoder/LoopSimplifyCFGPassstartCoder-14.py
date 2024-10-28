
```c
#include <stdio.h>

int main() {
    int x = 10; // declare and initialize x
    int y = 20; // declare and initialize y

    // A loop with a condition that can be constant-folded
    while (x < 100) {
        // Perform some operations
        x = x - y; // x is updated with an operation involving y
    }

    return x; // return the result
}
```
