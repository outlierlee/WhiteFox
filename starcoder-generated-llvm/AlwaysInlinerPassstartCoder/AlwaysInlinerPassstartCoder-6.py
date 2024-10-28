
```c
#include <stdlib.h>
#include <stdio.h>

inline int inline_func(int a, int b) {
  int va = abs(a);
  int vb = abs(b);
  int s = va * vb;
  int d = abs(a - b);
  double ratio = (double)s / (double)d;
  return ratio;
}

int main() {
  int result = 0;
  int x = -15;
  int y = 10;
  result = inline_func(x, y);
  return result;
}
```

