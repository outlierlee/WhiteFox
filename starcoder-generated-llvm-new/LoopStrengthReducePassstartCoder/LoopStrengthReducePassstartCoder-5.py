
```c
#include <stdio.h>

int main() {
    int sum = 0;
    int i;
    for (i = 0; i < 1E8; i++) {
        sum += (i & 1) ? (i * 32 + 15) : (i - 15);
    }
    printf("Sum: %d\n", sum);
    return sum % 10;
}
```

