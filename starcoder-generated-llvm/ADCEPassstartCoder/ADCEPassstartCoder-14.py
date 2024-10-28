
```c
#include <stdio.h>

static int a = 2;
static int b = -1;
static int c = 0;

static int compute(int x, int y, int z) {
  int result = x - y * z;
  return result;
}

int main() {
  int main_result = 0;

  a = a * 2;
  b = b + 1;

  if (a < 0) {
    a = -a;
  }

  if (b < 0) {
    b = -b;
  }

  if (a > b) {
    main_result = compute(a, b, 2);
  } else {
    main_result = compute(b, a, 3);
  }

  printf("Result: %d\n", main_result);
  
  return main_result;
}
```
# C Code ends