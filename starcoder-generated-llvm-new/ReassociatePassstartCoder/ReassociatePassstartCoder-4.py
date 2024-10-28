
```cpp
#include <stdio.h>

int a = -20;
int b = 10;
int c = 80;

int main() {
  int result = 0;
  result = (a + b) + c;
  result = (result * a) * b;
  result = (result - c) - a;
  printf("%d\n", result);
  return 0;
}
```
