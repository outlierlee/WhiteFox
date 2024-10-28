
```c
#include <stdio.h>

static void pointer_func(int *a, float *b, double *c) {
  if (a && b && c) {
    *a = 0;
    *b = (float)(*a);
    *c = (double)(*a);
  }
}

static void indirect_func(void) {
  int arr[5] = {1, 2, 3, 4, 5};
  int *ip = &arr[0];
  pointer_func(ip, (float *)&arr[1], (double *)&arr[2]);
}

int main() {
  int x = 10;
  float y = 5.5f;
  double z = 20.0;

  pointer_func(&x, &y, &z);
  indirect_func();

  printf("x: %d, y: %.2f, z: %.2f\n", x, y, z);

  return 0;
}
```

