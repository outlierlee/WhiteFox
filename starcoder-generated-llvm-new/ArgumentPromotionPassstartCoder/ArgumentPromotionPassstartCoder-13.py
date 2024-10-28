
```c
#include <stdio.h>

static int varargs_func(int x, ...) {
  return x;
}

int main() {
  int x = 10;
  float y = 5.5f;
  double z = 20.0;

  void *ptr = &x;

  // Call the function with a pointer argument
  varargs_func(*((int *)ptr), y, z);

  // Print the results
  printf("x: %d, y: %.2f, z: %.2f\n", x, y, z);

  return 0;
}
```
