
```c
#include <string.h>

typedef struct {
  char data[1024];
} LargeData;

int main() {
  LargeData source, destination;

  memset(&source, 0x5, sizeof(LargeData));
  memcpy(&destination, &source, sizeof(LargeData));

  if (destination.data[0] == 0x5) {
    // Do something
  }

  return 0;
}
```

