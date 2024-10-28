
```c
#include <stdio.h>

static inline int simple_func(int a, int b) {
  return a - b;
}

int main() {
  int a = 5;
  int b = 10;
  int c = simple_func(a, b);
  int d = 5;
  d += simple_func(c, d) + 5;
  return d;
}
```
