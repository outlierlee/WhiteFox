
```c
#include <stdio.h>

int a = 3;
int b = 5;
int c = 7;

int main() {
  int result = 0;

  result = (a + b) + c;
  result = (result * a) * b;
  result = (result - c) - a;

  printf("%d\n", result);

  return 0;
}
```
