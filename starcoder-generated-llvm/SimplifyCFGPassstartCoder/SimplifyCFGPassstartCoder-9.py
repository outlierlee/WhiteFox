
```c
#include <stdio.h>

int main() {
    int x = 0; // declare and initialize a variable
    int y = 1; // declare and initialize another variable

    // A simple conditional structure that creates an unreachable block
    if (x > y) {
        // This block is unreachable because x is not greater than y
        printf("Unreachable block\n");
        // A loop with an always occurring condition.
        // If this can ever be executed, it's considered unreachable.
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                printf("This has a chance to unreachable\n");
            }
        }
    } else {
        // This block is reachable
        printf("Reachable block\n");
    }

    // A loop that never executes, creating another unreachable block
    while (x > y) {
        printf("Unreachable loop block\n");
    }

    return 0;
}
```

