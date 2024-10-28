
```c
#include <stdio.h>

unsigned int a = 0xFU; // declare a
unsigned int b = 0x3U; // declare b
unsigned int c = 0xDU; // declare c
unsigned int d = 0x2U; // declare d

int main() {
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

