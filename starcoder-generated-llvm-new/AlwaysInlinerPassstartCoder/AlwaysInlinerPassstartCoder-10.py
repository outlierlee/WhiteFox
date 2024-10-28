
```c
#include <stdio.h>

inline int inline_func(int a, int b) {
  return a + b;
}

int main() {
  int result = 0;
  int x = 100;
  int y = 200;
  result = inline_func(x, y);
  return result;
}
```

