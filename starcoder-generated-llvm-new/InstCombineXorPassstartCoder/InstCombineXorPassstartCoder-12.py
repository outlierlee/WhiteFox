```c
#include <stdio.h>

int main() {

  int a = (1UL << 31);

  int b = 18, c=25, d=1.000000 ;

  int or1 = a | b;
  int or2 = a | c;

  int result = or1 ^ or2;

  printf("%d\n", result);

  return 0;
}
```
