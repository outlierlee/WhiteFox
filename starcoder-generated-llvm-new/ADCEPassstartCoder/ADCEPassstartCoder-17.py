
```c
#include <stdio.h>

// declare variables
int a = 100; // declare and initialize a
int b = 200; // declare and initialize b
int c = 0;  // declare and initialize c

// define a function that performs some operations
int compute(int x, int y) {
  int result = x*y; // perform an operation that is not used later
  return result; // return the result
}

int main() {
  int main_result = 0; // declare the result

  // perform some operations
  c = a + b; // perform an operation that is not used later

  // invoke the compute function
  main_result = compute(a, b);

  // print the result
  printf("Result: %d\n", main_result);

  return main_result; // return the result
}
```

