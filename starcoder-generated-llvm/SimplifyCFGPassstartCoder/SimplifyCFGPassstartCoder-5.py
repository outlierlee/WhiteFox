
```c
#include <stdio.h>

int main() {
    unsigned int x = (1ULL << 31);
    unsigned long long y = (1ULL << 63);

    printf("x: %llu\n", x);
    printf("y: %llu\n", y);

    if (x > y) {
        printf("%llu is greater than %llu\n", x, y);
    } else {
        printf("%llu is less than or equal to %llu\n", x, y);
    }

    for (; x >= y; x--) {
        printf("%llu is less than or equal to %llu\n", x, y);
    }

    return 0;
}
```
