
```c
#include <stdio.h>

int a = 10;
int b = 20;
int c = 30;

int main() {
  int result = 0;

  result = (a + b) + c;
  result = (result * a) * b;
  result = (result - c) - a;

  printf("%d\n", result);

  return 0;
}
```

