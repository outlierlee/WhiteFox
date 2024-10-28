
```c
#include <stdio.h>

int a = 0x7FFFFFFF; // assign a large number
int b = 1; // assign a small number
int c = 0;

int multiply(int x, int y, int z) {
  int result = 100;
  if (x % 2) {
    result = x * y + z;
  } else {
    result = x - y + z;
  }
  return result;
}

int main() {
  int main_result = 0;
  c = a + b + multiply(a, b, 5);
  main_result = multiply(a, b, 5);
  printf("%d\n", main_result);
  return 0;
}
```
