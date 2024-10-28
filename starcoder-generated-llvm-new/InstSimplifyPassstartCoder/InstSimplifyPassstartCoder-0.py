
```cpp
#include <stdio.h>

const int SIZE = 100;

int main() {
  int a = 10;
  int b = 2;

  if (b != 0) {
    int result = a / b;
    printf("Result: %d\n", result);
  } else {
    printf("Error: Division by zero\n");
  }

  int redundant = a * 1;
  printf("Redundant: %d\n", redundant);

  return 0;
}
```

