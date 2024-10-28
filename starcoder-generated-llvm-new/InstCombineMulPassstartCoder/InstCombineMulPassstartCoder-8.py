
```c
#include <stdio.h>

int main() {
    int x = 10;
    int result = x * (1 << 3); // multiplication is transformed into left shift by the compiler

    printf("%d\n", result); // print the result
    return 0; // terminate program successfully
}
```

