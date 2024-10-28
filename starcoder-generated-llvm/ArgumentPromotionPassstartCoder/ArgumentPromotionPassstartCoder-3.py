
```c
#include <stdio.h>

static void pointer_func(int *a, float *b, double *c) {
  if (a) *a -= 88;
  if (b) *b += 0.02f;
  if (c) *c -= 0.000001;
}

int main() {
  int x = (1 << 16) + 1;
  float y = (float)(1 << 16) + 0.5f;
  double z = (double)(1 << 16) + 0.000005;
  pointer_func(&x, &y, &z);
  printf("x: %d, y: %.6f, z: %.6f\n", x, y, z);
  return ((x << 16) + y + z) * 52 % 63;
}
```
