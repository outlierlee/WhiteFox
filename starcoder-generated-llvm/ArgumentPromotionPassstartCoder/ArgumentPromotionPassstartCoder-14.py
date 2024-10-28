
```c
#include <stdio.h>

static void pointer_func(int *a, float *b, double *c) {
  if (a) *a *= 3;
  if (b) *b /= 2.0f;
  if (c) *c -= 5.0;
}

int main() {
  int m = -5;
  float n = -5.5f;
  double p = -20.0;

  pointer_func(&m, &n, &p);

  printf("%d %.2f %.2f\n", m, n, p);

  return 0;
}
```

