
```c
#include <stdio.h>

int main() {
    float a = 3.141592f;
    float b = 6.283185f;
    float c = 12.566371f;
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

