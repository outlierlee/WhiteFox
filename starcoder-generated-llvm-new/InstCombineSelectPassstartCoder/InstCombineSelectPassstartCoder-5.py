
```c
#include <stdio.h>

int main() {
    float a = 3.14159;
    float b = 2.71828;
    float c = 1.41421;
    float result;

    if (a > b) {
        result = a;
    } else {
        result = b;
    }
    
    result = (a > b) ? a : b;

    printf("Result: %f\n", result);

    return 0;
}
```

