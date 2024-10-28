
```c
#include <stdio.h>

static void pointer_func(int *x, int *y, int *z, int t, float u, double v) {
  if(x) *x = *x + 1;
  if(y) *y = *y * 2;
  if(z) *z = *z - 3;
  ++t;
  u = u * 1.5f;
  v = v / 1.75;
}

int main() {
  int x = 10, y = 20, z = 30;
  int* px = &x;
  int* py = &y;
  int* pz = &z;

  pointer_func(px, py, pz, x, (float)y, (double)z);

  printf("x: %d, y: %d, z: %d\n", x, y, z);

  return 0;
}
```
