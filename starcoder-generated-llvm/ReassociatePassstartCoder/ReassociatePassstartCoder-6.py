
```c
#include <stdio.h>

int a = 24;
int b = 42;
int c = -19;

int main() {
  int result = 0;

  result = (a + b) + c;
  result = (result * a) * b;
  result = (result - c) - a;

  printf("%d\n", result);

  return 0;
}
```
