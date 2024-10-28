
```c
#include <stdlib.h>
#include <string.h>

int main() {
  char *buffer = (char *)malloc(100);
  if (!buffer) return -1;
  memset(buffer, 'A', 100);
  int num = 5;
  memset(buffer, 'B', num);
  free(buffer);
  return 0;
}
```
