
```c
#include <stdio.h>

int a = 42;
int b = 1337;
int c = -5;

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

