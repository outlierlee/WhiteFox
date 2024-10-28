
```c
#include <stdio.h>

int main() {
    float a = 3.14159; 
    float b = 4.2069; 
    float c = 100.0; 
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

