
```c
#include <stdio.h>

// declare variables
int a = (1 << 31);
int b = 123456;
int c = 234567;

int main() {
  int result = 0;

  // perform a series of arithmetic operations
  result = (a + b) + c;
  result = (result * a) * b;
  result = (result - c) - a;

  // use the result in a way that it is not trivially dead
  printf("%d\n", result);

  return 0;
}
```

