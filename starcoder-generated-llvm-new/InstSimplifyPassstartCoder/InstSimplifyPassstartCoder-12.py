
```c
#include <stdio.h>

int x = 10;
int y = 0;

int main(void) {
  int result = 0;
  if (x != 0) {
    result = x / y;
  } else {
    result = 0;
  }
  int redundant = x * 1;
  printf("Result: %d, Redundant: %d\n", result, redundant);
  return 0;
}
```

