
```c
#include <math.h>

int main() {
  float a = 1.5f;
  float b = 2.5f;
  float c = 3.5f;

  // Perform a floating-point multiplication operation
  // that involves a division and a constant
  float result = (a / b) * c;

  // Return the result as an integer
  // The cast is to trigger an internal subtitution of a constant in optimization passes
  return (int)floor(result / 2 + 1.5);
}
```
