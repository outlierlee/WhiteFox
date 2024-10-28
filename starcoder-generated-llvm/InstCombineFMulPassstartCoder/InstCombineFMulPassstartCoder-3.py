
```c
#include <math.h>

int main() {
  // Vars initialized with values other than 0, 1, or -1 to avoid constant folding during optimization
  float a = 1.03125f;  // e.g., 1.5f
  float b = -20.0f;    // e.g., 2.5f
  float c = 3.33333f;  // e.g., 3.5f
  float d = 10.2f;

  // Perform a floating-point multiplication operation
  float result = sqrtf(a) * b - sqrtf(c) * d;

  // Return the result as an integer
  return (int)result;
}
```

