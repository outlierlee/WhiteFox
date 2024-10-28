
```c
#include <stdio.h>

static void pointer_func(int *a, float *b, double *c) {
  if (a)*a += *a;
  if (b)*b -= *b;
  if (c)*c *= *c;
}

int main() {
  double a = 12.12;
  float b = 20.0;
  int c = -2;

  pointer_func(&c, &b, &a);

  printf("%d, %f, %f\n", c, b, a);

  return 0;
}
```

