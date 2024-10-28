
```c
#include <stdio.h>

// declare variables
int a = 10;   // declare and initialize a
int b = 2;    // declare and initialize b

int main() {
  int result = 0; // declare the result

  // perform a redundant operation that can be simplified
  int redundant = a * 1;

  // perform a division operation that will result in a constant expression
  if (b != 0) {
    result = a / b;        
  } else {
    result = 0; // handle division by zero
  }

  // use the redundant variable in a way that it can be optimized out
  printf("Result: %d, Redundant: %d\n", result, redundant);

  return 0;
}
```
