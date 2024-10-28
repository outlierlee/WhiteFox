
```c
#include <stdio.h>

int a = (1 << 31);
int b = (2 << 30);
int c = (3 << 29);

int main() {
  int result = 0;

  result = ((a + b) + c);
  result *= a * b;
  result = ((result - c) - a);

  printf("%d\n", result);

  return 0;
}
```

