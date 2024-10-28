```c
#include <stdio.h>

int a = sizeof(int) * 2;
int b = 3 * sizeof(int);
int c = sizeof(int) * 3 + 1;

int main() {
  int result = 0;

  result = (a + b) + c;
  result = (result * a) * b;
  result = (result - c) - a;

  printf("%d\n", result);

  return 0;
}
```
