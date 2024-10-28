
```cpp
#include <stdio.h>

int a, b; // declare variables

int main() {
  a = 10;  // initialize a
  b = 2;   // initialize b

  int result = 0;  // declare the result
  int rmnd = 0;    // declare the redundant variable
  
  if (b != 0) {
    result = a / b * 2;  // simplification
  } else {
    result = 0;  // handle division by zero
  }

  rmnd = a * 2;  // multiplication by 2 is redundant

  printf("Result: %d, Redundant: %d\n", result, rmnd);

  return 0;
}
```

