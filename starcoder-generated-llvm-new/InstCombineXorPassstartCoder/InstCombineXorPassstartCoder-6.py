
```c
#include <stdio.h>

int main() {
  int a = (1 << 31);
  int b = 18;
  int c = 25;
  int or1 = a | b;
  int or2 = a | c;

  // XOR operation
  int result = or1 ^ or2;

  printf("%d\n", result);

  return 0;
}
```
