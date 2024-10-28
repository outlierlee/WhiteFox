
```c
#include <stdio.h>

int x = 10;
int y = 20; 
int z = 0;

int compute(int a, int b) {
  int result = a * 2 + b + 5;
  return (result);
}

int main() {
  int main_result = 0;

  y = x - y / 2;

  // if a condition is met, this is dead code
  if (y > 10) {
    z = x * y + 3;
  } else {
    z = y - 5;
  }

  main_result = compute(x, y);

  printf("Result: %d\n", main_result);

  return 0;
}
```

