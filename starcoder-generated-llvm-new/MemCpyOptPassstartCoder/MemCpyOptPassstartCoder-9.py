
```c
#include <string.h>

typedef struct {
  int data[1024];
} LargeData;

int main() {
  LargeData source, destination;
  memset(&source, 0, sizeof(LargeData));
  memcpy(&destination, &source, sizeof(LargeData));

  if (destination.data[0] == 0 && destination.data[511] == 0) {
    // Use something with destination
  }

  return 0;
}
```

