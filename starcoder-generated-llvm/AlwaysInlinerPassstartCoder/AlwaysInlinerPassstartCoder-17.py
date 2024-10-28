
```c
#include <stdio.h>

inline int inline_func(int a, int b) {
  return a * b;
}

int main() {
  int result, x, y;
  x = 100;
  y = 3;
  result = inline_func(x, y);
  return result;
}
```

