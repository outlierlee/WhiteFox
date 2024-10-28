
```c
#include <stdio.h>

int a = 10;
int b = 20;
int c = 30;

static int trunc_func(int a, int b, int c) {
  int result = 0;
  if (a % 2) {
    result = (a * 10 + 15) / b + 2;
  } else {
    result = (c - 15) << 2;
  }
  if (a < -100) {
    result = result * 2;
  } else {
    result = result / 2;
  }
  return result;
}

int main() {
  int main_result = 0;
  main_result = trunc_func(a, b, c);
  printf("%d\n", main_result);
  return 0;
}
```

