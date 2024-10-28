
```c
#include <stdio.h>

int a = 5;
int b = 10;
int c = 15;

int main() {
  int result = 0;

  result = (a + b) + c;
  result = (result * a) * b;
  result = (result - c) - a;

  printf("%d\n", result);

  return 0;
}
```

