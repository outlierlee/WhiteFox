```c
#include <stdio.h>

int main() {
  int x = 0;
  int y = 10;

  // A loop that is provably never executed
  while (x < 0) { // This loop condition is always false
    y = y * 2; // This operation is never executed
  }

  // After the loop, return the value in y
  return y;
}
```
