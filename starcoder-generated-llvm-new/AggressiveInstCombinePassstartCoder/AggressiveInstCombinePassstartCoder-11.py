
```c
#include <stdio.h>

static int trunc_func(int a, int b, int c) {
  int result = (a * b) / c;
  return result;
}

int main() {
  int a = 2234; int b = 453; int c = 5;
  int main_result = trunc_func(a, b, c);
  printf("%d\n", main_result);
  return 0;
}
```
