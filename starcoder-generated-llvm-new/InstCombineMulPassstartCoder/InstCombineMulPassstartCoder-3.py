
```c
#include <stdio.h>

int main() {
    int x = (1 << 31); 
    int result = 0;

    result = x * (1 << 5);

    printf("%d\n", result);

    return 0;
}
```

