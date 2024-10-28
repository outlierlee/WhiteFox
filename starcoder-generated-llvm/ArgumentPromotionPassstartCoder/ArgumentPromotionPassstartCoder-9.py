
```c
#include <stdio.h>

static void pointer_func(int *a, float *b, double *c, void *d, void (*f)(void)) {
  if (a) {
    *a += 1;
  }
  if (b) {
    *b *= 2.0f;
  }
  if (c) {
    *c -= 3.0;
  }
  if (d) {
    void (*funptr)(void) = d;
    if (funptr)
      funptr();
  }
}

static void func_to_call(void) {
  printf("Function to be called indirectly\n");
}

int main() {
  int x = 9;
  float y = 5.5f;
  double z = 20.0;
  void (*funptr)(void) = &func_to_call;

  pointer_func(&x, &y, &z, funptr, funptr);

  printf("x: %d, y: %.2f, z: %.2f\n", x, y, z);

  return x - y;
}
```

