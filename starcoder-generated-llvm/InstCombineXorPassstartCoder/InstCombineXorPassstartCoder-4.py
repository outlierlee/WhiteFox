
```cpp
#include <stdio.h>

int main() {
  int a = 0x1234, b = 0x1234, c = 0x4321, d;
  int or1 = a | b;
  int or2 = a | c;
  int result = or1 ^ or2;
  printf("%d\n", result);

  return 0;
}
```

