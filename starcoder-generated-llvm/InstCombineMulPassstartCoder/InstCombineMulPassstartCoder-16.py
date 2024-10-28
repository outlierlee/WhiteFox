
```c
#include <stdio.h>

int main() {
    // Declare variables
    int x = 100; // Initialize x with any integer value
    int result;

    // Perform a multiplication operation that can be transformed
    // into a left shift operation by the compiler
    result = x * (1 << 5); // Any Constant is a positive integer

    // Use the result in some way
    printf("%d\n", result);

    return 0;
}
```
