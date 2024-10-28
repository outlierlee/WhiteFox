
```c
#include <stdio.h>

// declare variables
int a = 5; // declare and initialize a
int b = 10; // declare and initialize b
int c = 0;  // declare and initialize c

// define a function that performs some operations
int compute(int x, int y) {
  int result = x * y; // perform an simple operation
  return result; // return the result
}

int main() {
  int main_result = 0; // declare the result

  // perform some operations
  c = a + b; // perform an operation that is used later

  // invoke the compute function
  main_result = compute(a, b);

  // print the result
  printf("Result: %d\n", main_result);

  return c; // return the result
}
```

