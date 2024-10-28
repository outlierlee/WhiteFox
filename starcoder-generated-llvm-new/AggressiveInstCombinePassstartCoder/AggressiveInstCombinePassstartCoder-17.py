
```c
#include <stdio.h>

int main() {
  int a = 10, b = 20, c = 30;
  int result;
  result = trunc_func(a, b, c);
  printf("%d\n", result);
  return 0;
}

static int trunc_func(int a, int b, int c) {
  int result;
  result = (a - b) >> 3 * c;
  return result;
}
```
