
```c
#include <stdio.h>

int main() {
  unsigned int a = 35; // declare a
  unsigned int b = 15; // declare b
  unsigned int c = 42; // declare c

  // perform bitwise OR operations
  unsigned int or1 = a | b;
  unsigned int or2 = a | c;

  // perform XOR operation
  unsigned int result = or1 ^ or2;

  // print the result
  printf("%u\n", result);

  return 0;
}
```

