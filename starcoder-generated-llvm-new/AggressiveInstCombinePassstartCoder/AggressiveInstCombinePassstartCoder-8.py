
```c
#include <stdio.h>

static int trunc_func(int a, int b, int c) {
  int result = 0;
  if (a % 2) {
    result = (int)(((float) a) + 1 / (float) b) - c;
  } else {
    result = (int)(((float) (a * b)) / c);
  }
  if (result > 100) {
    result = (int)(((float) result) * 2.0);
  } else {
    result = (int)(((float) result) * 2.0);
  }
  return result;
}

int main() {
  int result = 0, a = (1 << 30), b = 2, c = (1 << 30);
  result = trunc_func(a, b, c);
  printf("%d\n", result);
  return 0;
}
```
