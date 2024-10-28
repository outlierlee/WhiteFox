
```c
#include <string.h>

typedef struct {
  char data[12345];
} LargeData;

int main() {
  LargeData source, destination;

  memset(&source, 'a', sizeof(LargeData));

  memcpy(&destination, &source, sizeof(LargeData));

  if (destination.data[0] == 'a') {
    return 1;
  }

  return 0;
}
```
