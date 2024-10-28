
```c
#include <stdlib.h>

inline int inline_func(int a, int b) {
  int product = a * b;
  if (product > 0)
    return product * product;
  else
    return -product;
}

int main() {
  int result = 0;
  int x = rand() % 10;
  int y = rand() % 10;
  result = inline_func(x, y);
  return result;
}
```
