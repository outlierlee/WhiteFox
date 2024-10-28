
```c
#include <stdio.h>

int a = 1000; // declare a
int b = 2000; // declare b
int c = 3000; // declare c

int main() {
  int result = 0; // declare the result

  // perform a series of arithmetic operations
  result = (((a + b) + c) * a) * b; // associative operation
  result = (((result - c) - a) * a) - b; // yet another associative operation

  // use the result in a way that it is not trivially dead
  printf("%d\n", result);

  return 0;
}
```
