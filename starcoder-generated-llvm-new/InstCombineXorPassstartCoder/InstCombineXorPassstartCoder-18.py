
```c
#include <stdio.h>

unsigned int a = 0xAAAAAAAAu;
unsigned int b = 0xFFFFFFFFu;
unsigned int c = 0x0000FFFFu;
unsigned int d = 0x12345678u;

int main() {
  unsigned int or1 = a | b;
  unsigned int or2 = a | c;

  unsigned int result = or1 ^ or2;

  printf("%u\n", result);

  return 0;
}
```
