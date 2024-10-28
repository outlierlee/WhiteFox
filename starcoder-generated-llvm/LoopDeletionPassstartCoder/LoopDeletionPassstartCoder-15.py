
```c
#include <stdio.h>

int main() {

  int x = -1; // x is always negative
  int y = 100; // y is used in the loop body

  // A loop that is provably never executed
  while (x < 0) { // The condition is always false
    // Loop body
    y = y * 2; // Perform some operation on y
  }

  // Return a value related to the loop body
  return y;
}
```

