
```c
#include <stdio.h>

int main() {
    int limit = 10000; 
    int sum = 0; 

    for (int i = 0; i < limit; i = (i + 1) * 2 - 1) {
        sum += i;
    }

    printf("Sum: %d\n", sum);
    return sum;
}
```

