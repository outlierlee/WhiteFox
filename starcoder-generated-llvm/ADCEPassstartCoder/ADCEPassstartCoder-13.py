
```c
#include <stdio.h>

int a = 10;
int b = 20;
int c = 0;

int compute(int x, int y) {
  int result = x + y;
  return result;
}

int main() {
  int main_result = 0;
  c = a + b;
  main_result = compute(a, b);
  printf("Result: %d\n", main_result);
  return main_result;
}
```
