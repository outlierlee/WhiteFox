#include <stdio.h>

// Define a function with pointer arguments
static void pointer_func(int *a, float *b, double *c) {
  // Perform operations using the pointer arguments
  if (a) *a += 1;
  if (b) *b *= 2.0f;
  if (c) *c -= 3.0;
}

int main() {
  int x = 10;
  float y = 5.5f;
  double z = 20.0;

  // Call the function with direct pointer arguments
  pointer_func(&x, &y, &z);

  // Print the results
  printf("x: %d, y: %.2f, z: %.2f\n", x, y, z);

  return 0;
}
