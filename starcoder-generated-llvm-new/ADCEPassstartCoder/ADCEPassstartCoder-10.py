
```c
#include <stdio.h>

// declare variables
int a = 0;
int b = 1;
int c = 2;

// define a function that performs some operations
int compute(int x, int y) {
  int result = x + y;
  return result;
}

int main() {
  int main_result = 0;

  // perform some operations
  int tmp1 = (1 << 4);
  a = tmp1;

  int tmp2 = (1 << 3);
  b = tmp2;

  // invoke the compute function
  main_result = compute(a, c);

  printf("Result: %d\n", main_result);

  return main_result;
}
```


