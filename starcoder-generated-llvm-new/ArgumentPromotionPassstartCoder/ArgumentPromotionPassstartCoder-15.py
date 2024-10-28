
```c
#include <stdio.h>

static void pointer_func(int *a, int *b, int *c) {
 if (a) *a += *b + *c * 2;
 if (b) *b += 2;
 if (c) *c += *a - *b / 2;
}

int main() {
  int x, y, z;
  x = y = z = 10;
  if (x == 5) {
      y = 3 * x;
  } else {
      z = x + y;
  }
  int res = 0;
  if (y > 5) {
      res = y / x;
  } else {
      res = z %x;
  }
  pointer_func(&x, &y, &z);
  printf("x: %d, y: %d, z: %d\n", x, y, z);

  return res;
}
```

