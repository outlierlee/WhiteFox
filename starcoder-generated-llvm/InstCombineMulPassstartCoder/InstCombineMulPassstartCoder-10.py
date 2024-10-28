
```c
#include <stdio.h>

int main() {
    int x = (1 << 31); // Initialize x with the largest possible integer
    int result = x * (1 << 7); // Perform a shift operation

    // Use the result in some way
    printf("%d\n", result);

    return 0;
}
```
