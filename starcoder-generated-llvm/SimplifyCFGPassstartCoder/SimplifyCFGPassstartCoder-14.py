
```c
#include <stdio.h>

int main() {
    int x = 1;
    int y = 1;

    // create unreachable block
    if (x > y) {
        printf("Unreachable block\n");
    } else {
        printf("Reachable block\n");
    }

    // create unreachable loop block
    while (x > y) {
        printf("Unreachable loop block\n");
    }

    return 1; // should return 1 to trigger optimization
}
```
