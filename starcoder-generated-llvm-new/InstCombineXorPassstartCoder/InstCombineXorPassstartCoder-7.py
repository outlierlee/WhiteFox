
```c
#include <stdio.h>

int main() {
  int a = 0x12345678;
  int b = 0xFF121111;
  int c = 0xAABBCCDD;
  int d = 0xABCABCDA;

  int or1 = a | b;
  int or2 = a | c;

  int result = or1 ^ or2;

  printf("%x\n", result);

  return 0;
}
```
