
```c
#include <stdio.h>

int main() {
    float a = 10.1f;
    float b = 15.15f;
    float c = 16.16f;
    float result;
  
    if (a > b) {
        result = a;
    } else {
        result = b;
    }

    result = (a > b) ? a : b;

    printf("Result: %f\n", result);

    return result;
}
```

