
```c
#include <stdio.h>

int a = 1000; // declare and initialize with large numbers to make division operation slow
int b = 0;

int main() {
  int result = 0;
  result = a;
  if (b != 0) {
    result = a / b;
  } else {
    result = 0;
  }
  int redundant = a + 1;
  printf("Result: %d, Redundant: %d\n", result, redundant);
  return 0;
}
```
