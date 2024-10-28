
```c
#include <stdio.h>

int main() {
    int x = 21;
    int result = 0;

    // The multiplication operation can be transformed
    // into a left shift operation
    result = x * (1 << 3);

    printf("%d\n", result);

    return 0;
}
```
