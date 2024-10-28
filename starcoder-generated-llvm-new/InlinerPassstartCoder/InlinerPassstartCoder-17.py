
```c
#include <stdio.h>

static inline int inlined_function(int a, int b) { 
    return a + b; 
}

int main() {
    int x = 10, y = 20;
    int result = 0;
    result = inlined_function(x, y);
    return result;
}
```

