
```c
#include <stdio.h>

int main() {
  int a = 10;
  int b = 20;
  int c = 30;
  int d = 40;

  int or1 = a | b;
  int or2 = a | c;

  int result = or1 ^ or2;

  printf("%d\n", result);

  return 0;
}
```

