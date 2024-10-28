
```c
#include <stdio.h>

int a = (1 << 31);
int b = (1 << 30);
int c =  (1 << 29);

int main() {
  int result = 0;

  result = (a + b) + c;
  result = (result * a) * b;
  result = (result - c) - a;

  printf("%d\n", result);

  return 0;
}
```
