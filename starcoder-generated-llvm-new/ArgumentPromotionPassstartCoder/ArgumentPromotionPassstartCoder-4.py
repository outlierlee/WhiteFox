
```cpp
#include <stdio.h>

static void pointer_func(int *a, float *b, double *c) {
  if (a) *a *= 2;
  if (b) *b = 0;
  if (c) *c = *a + *b;
}

int main() {
  int x = 100;
  float y = 5.5f;
  double z = -20.0;

  pointer_func(&x, &y, &z);

  printf("x: %d, y: %.2f, z: %.2f\n", x, y, z);

  return x * x;
}
```

# Explaination of Code
The rule that `main` function must return a value related to the optimization is followed. The result is computed by returning the square of `x`, which is a value that is equivalent to `x` itself.
The `pointer_func` is a function which modifies the values of the pointer arguments. It does not depend on the values of the pointer arguments, Hence, there will be no undefined behavior and no variable arguments.
The arguments to `pointer_func` are pointers which points to address of `x`, `y`, `z` in `main` function respectively and these pointers are mutated.
After the call to `pointer_func`, the values of `x`, `y`, `z` get updated according to the rules in `pointer_func`, hence accordingly in `main` `printf("x: %d, y: %.2f, z: %.2f\n", x, y, z);` will print the updated values.