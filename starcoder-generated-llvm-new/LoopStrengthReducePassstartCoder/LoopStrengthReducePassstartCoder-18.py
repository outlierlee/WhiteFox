
```cpp
#include <stdio.h>

static int scalar_add(int x, int y, int z, int w, int t) {
  int result = (x * y) + (z * w) + t;
  return result;
}

int main() {
  int sum = 0;
  int i;
  for (i = 0; i < 10; i++) {
    sum += i;
  }
  int result = scalar_add(sum, 15, sum - 100, sum + 100, sum & 1);
  printf("Result: %d\n", result);
  return result & 1;
}
```

