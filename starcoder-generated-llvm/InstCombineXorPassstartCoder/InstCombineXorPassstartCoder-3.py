
```c
#include <stdio.h>

int main() {
    int a = 0xFFFFFFFF;
    int b = 0x55555555;
    int c = 0xAAAAAAAA;
    int d = 0xCCCCCCCC;

    int or1 = a | b;
    int or2 = a | c;

    int result = or1 ^ or2;

    printf("%d\n", result);

    return 0;
}
```

