
```c
#include <stdio.h>

int main() {
    float a = 1.23f;
    float b = 2.34f;
    float c = 3.45f;
    float result;

    if (a < b) {
        result = a;
    } else {
        result = b;
    }

    result = (a < b) ? a : b;
    
    printf("Result: %f\n", result);

    return 0;
}
```
