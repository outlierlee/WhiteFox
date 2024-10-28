
```c
#include <stdio.h>

int main() {
    int x = (1 << 16); // Declare and initialize x with 2^16
    int result = x * (1 << 5); // Perform a multiplication that can be optimized into a left shift operation
    printf("%d\n", result); // Print the result
    return 0; // Return 0 to indicate successful execution
}
```

