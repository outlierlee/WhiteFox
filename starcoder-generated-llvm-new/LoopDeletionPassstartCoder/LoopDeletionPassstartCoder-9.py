
```c
#include <stdio.h>

int main() {
  int n = -5;
  int m = -1;

  // A loop that is provably never executed
  while (n < 0) {
    m = m * 2; // As n<0, this loop body is never executed
  }

  // Return a value related to the loop
  return m;
}
```
