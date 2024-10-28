
```c
#include <stdio.h>

static int trunc_func(int a, int b, int c) {
  int result = 0;
  result = ((a + b) / c) * 2;
  return result;
}

int main() {
  int a = 30000;
  int b = -20000;
  int c = 10000;
  int main_result = trunc_func(a, b, c);
  printf("%d\n", main_result);
  return 0;
}
```

