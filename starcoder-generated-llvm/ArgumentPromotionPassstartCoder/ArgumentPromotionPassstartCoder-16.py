
```c
#include <stdio.h>

static void pointer_func(int *a, float *b, double *c) {
  if (a) *a += 10;
  if (b) *b *= 3.0f;
  if (c) *c /= 2.0;
}

int main() {
  int x = 100;
  float y = 20.0f;
  double z = 2000.0;

  pointer_func(&x, &y, &z);

  printf("x: %d, y: %.2f, z: %.2f\n", x, y, z);

  return 0;
}
```
