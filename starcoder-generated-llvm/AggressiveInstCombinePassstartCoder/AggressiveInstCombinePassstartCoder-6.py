
```c
#include <stdio.h>

static int trunc_func(int a, int b, int c) {
  int result = 0;
  if (a > b) {
    result = a - b;
  } else {
    result = b - a;
  }
  if (result > 100) {
    result = result % 2 + 1;
  } else {
    result = result * (b - a);
  }
  result = result % c;
  return result;
}

int main() {
  int a = 10, b = 20, c = 5, main_result = 0;
  main_result = trunc_func(a, b, c);
  printf("%d\n", main_result);
  return 0;
}
```

