
```c
#include <stdio.h>

static inline int simple_function(int a, int b) {
  return a * a + b; // New operation for testing
}

int main() {
  int i, j, k = 1;
  int result = 0;
  for(i = 0; i < 10; i++){
    short x=10-k; 
    simple_function(i, x);
    result += simple_function(x, x);
  }
  return result;
}
```

