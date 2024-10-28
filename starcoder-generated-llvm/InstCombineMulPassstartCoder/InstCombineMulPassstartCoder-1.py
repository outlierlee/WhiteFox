
```c
#include <stdio.h>

int main() {
    // Declare variables
    int x = 5; // Initialize x with any integer value
    int result;

    // Perform a multiplication operation that can be transformed
    // into a left shift operation by the compiler
    result = x * (1 << 4); // Compiler can replace this multiplication with a left shift

    // Use the result in some way
    printf("%d\n", result);

    return 0;
}
```

