
```c
#include <stdio.h>

static void pointer_func(void *a, void *b, void *c) {
  int *xa = (int *)a;
  float *ya = (float *)a;
  double *za = (double *)a;
  if (xa) *xa += 1;
  if (ya) *ya *= 2.0f;
  if (za) *za /= 3.0;
}

int main() {
  int x = 10;
  float y = 5.5f;
  double z = 20.0;

  pointer_func(&x, &y, &z);

  printf("x: %d, y: %.2f, z: %.2f\n", x, y, z);

  return 0;
}
```

