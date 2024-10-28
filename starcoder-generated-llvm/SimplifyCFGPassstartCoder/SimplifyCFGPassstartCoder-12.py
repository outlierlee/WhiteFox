
```c
#include <stdio.h>

int main() {
    int x = 1;
    int y = 1;
    bool x_larger_than_y = (x > y);
    if (x_larger_than_y) {
        printf("Unreachable, x is not larger than y\n");
    } else {
        printf("Reachable, x is smaller than y\n");
    }
    while (x > y) {
        printf("Unreachable, x is not larger than y\n");
    }
    return 0;
}
```
