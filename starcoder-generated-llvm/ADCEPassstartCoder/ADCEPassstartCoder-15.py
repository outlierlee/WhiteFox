
```c
#include <stdio.h>

int a = 0x42;
int b = 0x5A;
int c = 0xFF;
int d = 0;
int e = 0;
int f = 0;

int compute_compute(int x, int y) {
  int res = 0;
  if (x == 0x42) {
    if (y % 5) {
      res = x + y;
    } else {
      res = x - y;
    }
  } else {
    res = x * y;
  }
  return res;
}

int main() {
  int main_result = 0;

  c = a + b;
  d = (c >> 1) & 0xF;

  main_result = compute_compute(a, b);

  printf("Result: %u\n", main_result);

  return main_result;
}
```
