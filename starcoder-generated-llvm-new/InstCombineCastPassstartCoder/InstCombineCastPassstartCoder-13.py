
```c
#include <stdio.h>

int main() {
  float x = -2147483648.0f;
  unsigned int y = 18446744073709551615U;
  unsigned int result = (unsigned int) x + y;
  printf("%d\n", (int) result); 
  return 0;
}
```

