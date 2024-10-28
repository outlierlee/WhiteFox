```c
#include <stdio.h>

// declare variables
int a = 10; // declare a
int b = 5; // declare b
int c = 3; // declare c

int main() {
  int result = 0; // declare the result

  // perform a series of arithmetic operations
  result = (a + b) + c; // associative operation
  result = (result * a) * b; // another associative operation
  result = (result - c) - a; // yet another associative operation

  // use the result in a way that it is not trivially dead
  printf("%d\n", result); // print the result

  return 0;
}
```

