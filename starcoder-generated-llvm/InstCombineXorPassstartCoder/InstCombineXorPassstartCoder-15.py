
```c
#include <stdio.h>

int main() {

  int a = -1;
  unsigned int b = 0;
  long c = 1;
  unsigned long d = 2;

  int or1 = a | b;
  int or2 = a | (int)c;

  int result = or1 ^ or2;

  printf("%d\n", result);

  return 0;
}
```

