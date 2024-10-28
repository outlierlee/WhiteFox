
```c
#include <stdio.h>

int simple_conditional(int a, int b) {
  return (a % 2) ? b - b + a : b*a;
}

int main() {
  int x = (1 << 31) - 1;
  int y = 100;
  int result = 0;

  result = simple_conditional(x, y);

  if (result > 1000) {
    printf("Result is greater than 1000 (not reached)\n");
  } else {
    printf("Result is 1000 or less\n");
  }

  return result;
}
```

