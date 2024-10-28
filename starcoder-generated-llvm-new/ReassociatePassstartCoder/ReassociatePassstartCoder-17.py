
```c
#include <stdio.h>

int main() {
  int a = 10, b = 20, c = 30;
  int result;
  result = (a + b) + c;
  result = (result * a) * b;
  result = (result - c) - a;

  printf("%d\n", result);

  return 0;
}
```
