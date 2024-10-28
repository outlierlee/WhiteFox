```c
#include <stdio.h>

static inline int add(int a, int b) { return a + b; }

int main() {
  int x = 10, y = 20;
  int sum = add(x, y);
  return sum;
}
```
