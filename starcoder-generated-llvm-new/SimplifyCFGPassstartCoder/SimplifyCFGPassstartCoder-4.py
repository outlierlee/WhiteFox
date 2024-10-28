
```c
#include <stdio.h>

int main() {
    int a = 0;
    int b = 1;

    if (a > b) {
        printf("Unreachable block\n");
    } else {
        printf("Reachable block\n");
    }

    while (a > b) {
        printf("Unreachable loop block\n");
    }

    for (a = 0; a < 10; ++a) {
        if (a == 5) {
            continue;
        }
        printf("%d\n", a);
    }

    return 0;
}
```

