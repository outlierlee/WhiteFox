
```c
#include <stdio.h>

static void pointer_func(int *a, float *b, double *c) {
  if (a) *a += 1;
  if (b) *b = *b * 1.5;
  if (c) *c *= 1.25;
}

int main() {
  int x = 24;
  float y = 12.5f;
  double z = 20.0;

  pointer_func(&x, &y, &z);

  printf("x: %d, y: %.2f, z: %.2f\n", x, y, z);

  return 0;
}
```

# C Code ends