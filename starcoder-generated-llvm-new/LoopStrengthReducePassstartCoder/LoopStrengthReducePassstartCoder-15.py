
```c
#include <stdio.h>

int main() {
    int sum = 21;
    int loop = 21;
    int a = 20;
    int b = 5;
    int i;
    int j;

    for (i = 0; i < a; i++) {
        sum += i;
    }

    for (j = 0; j < b; j++) {
        loop += j;
    }

    printf("Sum: %d\n", sum + loop); 
    return 0;
}
```

