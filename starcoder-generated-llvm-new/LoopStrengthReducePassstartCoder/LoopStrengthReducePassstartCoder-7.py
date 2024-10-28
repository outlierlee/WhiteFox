
```cpp
#include <stdio.h>

int main() {
    int sum = 0;
    long i;

    for (i = 0; i < 10000000000; i++) {
        sum += i;
    }

    printf("Sum: %ld\n", sum);
    return sum;
}
```

