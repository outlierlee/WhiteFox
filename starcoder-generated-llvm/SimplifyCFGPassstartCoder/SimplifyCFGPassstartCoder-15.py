
```c
#include <stdio.h>

int main() {
    int x = 0; 
    int y = 1; 
    if (x < y) {
        printf("Reachable block\n");
    } else {
        printf("Unreachable block\n");
    }

    while (x < y) {
        printf("Unreachable loop block\n");
    }

    return 0;
}
```

