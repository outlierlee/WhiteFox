
```cpp
#include <stdio.h>

int x = 16<<2;

int main() {
  int result = (char) ((char) x + 25);
  printf("%d\n", (int) result);
  return 0;
}
```

