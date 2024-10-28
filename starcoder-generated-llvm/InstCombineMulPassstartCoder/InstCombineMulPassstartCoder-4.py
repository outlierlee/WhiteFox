
```cpp
#include <stdio.h>

int main() {
    int x = (1 << 31); // Because it involves exponentiation
    int result = x * (1 << 2);
    printf("%d\n", result);

    return 0;
}
```

