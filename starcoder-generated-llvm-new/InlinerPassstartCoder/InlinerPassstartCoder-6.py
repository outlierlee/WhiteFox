
```c
#include <stdio.h>

static inline int simple_function(int a, int b) {
   int c = 9;
   for (; c < a && c < b; c++);
   return c;
}

int main() {
   int x = 15;
   int y = 20;
   int result;
   result = simple_function(x, y);
   return result;
}
```

