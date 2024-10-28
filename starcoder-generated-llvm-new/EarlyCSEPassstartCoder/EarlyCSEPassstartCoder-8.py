
```cpp
#include <stdio.h>

int main() {
  // Declare and initialize variables
  int a = 16;
  int b = 32;
  int c = 64; // Same value as 'a' and 'b' to trigger common subexpression elimination
  int d = -32;

  // Perform operations that can be simplified or eliminated by recognizing common subexpressions
  int result1 = (a + b + c + d) / 4; // First computation, combined common subexpression
  int result2 = (a + b + c + d) / 4; // Second computation, identical to result1, optimized out

  // Use the results
  printf("Result1: %d\n", result1);
  printf("Result2: %d\n", result2);

  return 0;
}
```
