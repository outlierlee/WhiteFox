
```c
#include <stdio.h>

int main() {
  unsigned int a = 42;
  unsigned int b = 25;
  unsigned int c = 18;
  int d = 1;

  unsigned int or1 = a | b;
  unsigned int or2 = c | d;

  int result = or1 ^ or2;

  printf("%d\n", result);

  return 0;
}
```
