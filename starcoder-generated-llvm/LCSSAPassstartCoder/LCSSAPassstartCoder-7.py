
```c
#include <stdio.h>
#define ITERATION_COUNT (5)

int main() {
  int result = 0;
  int a = (1 << 31);

  for (int i = 0; i < ITERATION_COUNT; i++) {
    if (a & 1) {
      result += a;
    } else {
      result -= a;
    }
  }

  if (result > 0) {
    printf("Result is positive\r\n");
  } else {
    printf("Result is non-positive\r\n");
  }

  return result;
}
```
