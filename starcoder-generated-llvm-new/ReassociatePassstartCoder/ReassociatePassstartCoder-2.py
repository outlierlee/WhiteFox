
```cpp
#include <stdio.h>

// declare variables
int a = (1 << 31); // declare a
int b = (1 << 20); // declare b
int c = (1 << 10); // declare c

int main() {
  int result = 0; // declare the result

  // perform a series of arithmetic operations
  result = (a + b) + c; // associative operation
  result = (result * a) * b; // another associative operation
  result = (result - c) - a; // yet another associative operation

  // use the result in a way that it is not trivially dead
  printf("%d\n", result);

  return 0;
}
```
