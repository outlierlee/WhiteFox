
```c
#include <stdio.h>

int a = 10;
int b = 10;

int main() {
  int result = 0;

  if (b != 0) {
    result = a / b;
  } else {
    result = 1;
  }

  int redundant = a * 1;

  printf("Result: %d, Redundant: %d\n", result, redundant);

  return 0;
}
```
