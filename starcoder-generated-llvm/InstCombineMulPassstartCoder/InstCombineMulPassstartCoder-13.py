
```c
#include <stdio.h>

int main() {
    int x = 1024; // Given value
    int result;

    // Optimization: perform leftshift operation using multiplication
    result = x * 2; 

    printf("%d\n", result);

    return 0;
}
```

