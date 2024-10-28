
```c
#include <stdio.h>

// declare variables
int a = 100; // declare and initialize a
int b = 10;  // declare and initialize b

int main() {
  int result = 0; // declare the result

  // perform a meaningful operation
  if (b != 0) {
    result = a / b; // computation for efficiency
  } else {
    result = 0; // handle division by zero
  }

  // perform a redundant operation
  int redundant = a * 2; // multiplication by 2 is redundant

  // use the redundant variable in a way that it can be optimized out
  printf("Result: %d, Redundant: %d\n", result, redundant);

  return 0;
}
```

