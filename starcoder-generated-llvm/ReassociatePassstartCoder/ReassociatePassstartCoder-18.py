
```c
#include <stdio.h>

int a = 7;
int b = 15;
int c = 2;

int main() {
  int result = 0;

  result = (a + b) + c;
  result = (result * a) * b;
  result = (result - c) - a;

  printf("%d\n", result);

  return 0;
}
```

