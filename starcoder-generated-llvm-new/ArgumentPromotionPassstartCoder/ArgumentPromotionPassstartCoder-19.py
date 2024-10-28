
```cpp
#include <cstddef>
#include <iostream>

// Define a function with pointer arguments
static void pointer_func(int *a, float *b, double *c) {
  if (a != nullptr) *a += 1;
  if (b != nullptr) *b *= 2.0f;
  if (c != nullptr) *c -= 3.0;
}

int main() {
  int x = 10, * xp = nullptr;
  float y = 5.5f, * yp = nullptr;
  double z = 20.0, * zp = nullptr;

  // Call the function with direct pointer arguments
  pointer_func(&x, &y, &z);

  // Perform comparisons
  int sum = (x == 11 && y == 5.5f && z == 17.0) ? 1 : 0;

  // Print the results
  std::cout << "x: " << x << ", y: " << y << ", z: " << z << std::endl;

  return sum;
}
```

