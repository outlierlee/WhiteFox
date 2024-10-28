
```cpp
#include <stdio.h>

int main() {
    int x = 0;
    int y = 1;

    // A simple conditional structure that creates an unreachable block
    if (x > y) {
        printf("Unreachable block\n");
    } else {
        printf("Reachable block\n");
    }

    // A loop that never executes, creating an unreachable block
    while (x > y) {
        printf("Unreachable loop block\n");
    }

    return 0;
}
```

