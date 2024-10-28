
```cpp
#include <stdio.h>

int a = (1 << 31);
int b = 18;
int c = 25;

int main() {
  int or1 = a | b;
  int or2 = a | c;
  int result = or1 ^ or2;

  printf("%d\n", result);

  return 0;
}
```

