
```c
#include <math.h>

int main() {
  // Declare and initialize floating-point variables
  float a = 1.5f;
  float b = 2.5f;
  float c = sqrt(3.5f);

  // Perform a floating-point multiplication operation
  // that involves a constant and a variable
  float result = (a / b) * c; // This operation will trigger the optimization

  // Return the result as an integer
  return (int)result;
}
```
