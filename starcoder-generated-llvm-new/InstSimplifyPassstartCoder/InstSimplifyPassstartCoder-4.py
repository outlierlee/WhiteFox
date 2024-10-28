
```c
#include <stdio.h>

int a = 80;
int b = 4;

enum {
  ENUM_VAL1 = 1,
  ENUM_VAL2 = -1,
  ENUM_VAL3 = 0,
};

int main() {
  int result = 0;
  if (a / b != 0) {
    result = a / b + ENUM_VAL1;
  }
  else {
    result = a * ENUM_VAL2;
  }
  int redundant = (a >> (b + ENUM_VAL3)) + ENUM_VAL1;
  printf("Result: %d, Redundant: %d\n", result, redundant);
  return 0;
}
```
