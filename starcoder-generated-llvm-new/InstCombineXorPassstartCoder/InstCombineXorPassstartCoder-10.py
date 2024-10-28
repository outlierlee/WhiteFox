
```c
#include <stdio.h>

int main() {
  // declare variables
  int a = 10;
  int b = 20;
  int c = 30;
  int d = 40;

  // perform bitwise OR operations
  int or1 = a | b;
  int or2 = a | c;

  // perform XOR operation
  int result = or1 ^ or2;

  // print the result
  printf("%d\n", result);
  printf("%d\n", (a | b) ^ (a | c));

  return 0;
}
```

