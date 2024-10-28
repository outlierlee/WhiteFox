
```c
#include <stdio.h>

inline int inline_func(int a, int b) {
  return a + b;
}

int main() {
  int result = 0;
  int x = 10;
  int y = 5;
  result = inline_func(x, y);
  printf("%d", result);
  return 0;
}
```

