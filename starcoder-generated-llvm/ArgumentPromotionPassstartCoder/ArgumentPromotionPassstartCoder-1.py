
```c
#include <stdio.h>

static void pointer_func(int *a, float *b, double *c) {
  if (a) *a += 1;
  if (b) *b *= 2.0f;
  if (c) *c -= 3.0;
}

int main() {
  int x = 10;
  float y = 5.5f;
  double z = 20.0;

  x = x+2;
  y = y*2.0f;
  z = z-3.0;

  printf("x: %d, y: %.2f, z: %.2f\n", x, y, z);

  return 0;
}
```

