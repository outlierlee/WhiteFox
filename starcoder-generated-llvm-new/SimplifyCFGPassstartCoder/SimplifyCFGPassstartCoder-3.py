
```c
#include <stdio.h>

int main() {
    int x = 0;
    int y = 1;

    if (x > y) {
        printf("Unreachable block\n");
    } else {
        printf("Reachable block\n");
    }

    while (x > y) {
        printf("Unreachable loop block\n");
    }

    return 0;
}
```

