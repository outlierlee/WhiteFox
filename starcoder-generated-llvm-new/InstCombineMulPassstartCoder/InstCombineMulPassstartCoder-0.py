
```c
#include <stdio.h>

int main() {
    // Declare variables
    int x = (1 << 31); // This example uses a specific power of two value
    int result;

    // Perform a multiplication operation that can be transformed
    // into a shift operation by the compiler
    result = x * (1 << 2); // This example also uses a specific power of two value

    // Print the result
    printf("%d\n", result);

    return 0;
}
```
