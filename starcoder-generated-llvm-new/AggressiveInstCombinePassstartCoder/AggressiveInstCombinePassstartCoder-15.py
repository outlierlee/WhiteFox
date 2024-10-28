
```c
#include <stdio.h>

int a = 49;
int b = 10;
int c = 2;

static int trunc_func(int a, int b, int c) {
  int result = 0;
  result = (a + b) / c;
  return result;
}

int main() {
  int main_result = 0;
  main_result = trunc_func(a, b, c);
  printf("%d\n", main_result);
  return 0;
}
```

