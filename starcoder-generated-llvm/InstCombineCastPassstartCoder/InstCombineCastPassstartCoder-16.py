
```cpp
#include <stdio.h>

int main() {
  unsigned int x = 1 << (sizeof(unsigned int) * 8 - 1);
  unsigned int result = (unsigned int) x;
  printf("%d\n", (int) result); 
  return 0;
}
```

