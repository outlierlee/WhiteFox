
```c
#include <stdio.h>

int main() {
    // Initialiaze an integer
    int x = -26;
    int result;

    // Perform a multiplication operation that can be transformed
    // into a left shift operation by the compiler
    result = x * (1 << 3);

    // Use the result in some way
    printf("%d\n", result);

    return 0;
}
```

