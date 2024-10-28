
```c
#include <stdio.h>

int main() {
    int sum = 0;
    unsigned int i;
    const int n = 100;
    int a[105] = {3, 5, 7, 11, 13};

    for (i = 4; i < 100; i++) {
        sum += i + a[i];
    }
    
    a[n] = a[n] % 2 == 0 ? sum * 2 : sum - 5;
    
    printf("Sum: %d\n", sum + a[i]);
    return sum;
}
```

