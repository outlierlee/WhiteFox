
```cpp
#include <stdio.h>

int main() {
  int result = 0;
  int arr[4] = {1, 2, 3, 4};
  int mask = 0;
  for(int i = 0; i < 4; i++) {
    mask = mask | (1 << (3 - i));
    result ^= (arr[i] + mask);
  }
  printf("Result: %d\n", result);
  return result;
}
```

