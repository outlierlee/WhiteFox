
```c
#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;

    // A loop which can be constant-folded
    while (a < b) {
        // Perform some operations
        a = a + 1; // a is updated with an operation involving b
    }

    return a; // return the result
}
```

