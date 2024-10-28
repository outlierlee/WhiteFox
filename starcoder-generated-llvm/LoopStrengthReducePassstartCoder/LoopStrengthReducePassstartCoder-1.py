
```c
#include <stdio.h>

int main() {
    int sum = 0;
    int i = 30;

    while(i < 100) {
        sum += (i ^ 2);
        i += 2;
    }

    printf("Sum: %d\n", sum);
    return sum;
}
```

