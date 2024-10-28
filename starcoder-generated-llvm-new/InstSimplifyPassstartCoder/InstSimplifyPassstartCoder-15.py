
```c
#include <stdio.h>

int a = 0x42; // declare and initialize a to a constant expression
int b = 0x2;  // declare and initialize b to a constant expression

int main() {
  int result = 0; // declare the result

  // perform a division operation that will result in a constant expression
  if (b != 0) {
    result = a / b; // this division will be simplified
  } else {
    result = 1; // handle division by zero
  }

  // perform a multiple operation
  int redundant = a * 1; // multiplication by 1 is redundant

  // use the `result` variable in a way that it can be optimized out
  printf("Result: %d, Redundant: %d\n", result, redundant);

  return 0;
}
```

