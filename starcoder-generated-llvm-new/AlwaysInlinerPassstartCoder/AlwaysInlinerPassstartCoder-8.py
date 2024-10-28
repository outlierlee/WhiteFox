
```c
#include <stdio.h>
#include <stdlib.h>

inline int sum(int a, int b) {
  return a + b;
}

int main() {
  int x = 10;
  int y = 20;
  int z = sum(x, y);
  printf("\nSum: %d", z);
  return z;
}
```

