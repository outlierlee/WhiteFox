
```c
#include <stdio.h>

int main() {
    long a = 5;
    long b = 10;
    long c = 5; 

    long result1 = 0;
    long result2 = 0;
    long result3 = 0;

    for(long i = 0; i < 100000000; i++)
    {
        result1 = a + b;
        result2 = c + b;
        result3 = result1 + result2;
    }

    printf("Result1: %ld\n", result1);
    printf("Result2: %ld\n", result2);
    printf("Result3: %ld\n", result3);

    return 0;
}
```

