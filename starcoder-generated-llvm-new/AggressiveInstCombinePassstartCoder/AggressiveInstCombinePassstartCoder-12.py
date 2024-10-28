```c
#include <stdio.h>

static int trunc_func(int a, int b, char c) {
  int result = 0;
  if (a > b) {
    result = (a - b) / c;
  } else {
    result = (b - a) / c;
  }
  return result;
}

int main() {
  int main_result = 0;
  int a = 1024;
  char b = -128;
  char c = 32;
  main_result = trunc_func(a, b, c);
  printf("%d\n", main_result);
  return 0;
}
```
