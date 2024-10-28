
```c
#include <stdio.h>

int main() {
  long a = (1 << 31);
  char b = '1';
  int result = (unsigned char)(a + b);
  printf("%d\n", (int) result);
  return 0;
}
```
