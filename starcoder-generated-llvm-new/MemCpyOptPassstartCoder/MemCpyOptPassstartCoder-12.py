
```c
#include <string.h>

typedef struct {
  char large_data[10000000];
} LargeData;

int main() {
  LargeData source, destination;

  memset(&source, 'A', sizeof(LargeData));

  memcpy(&destination, &source, sizeof(LargeData));

  if (destination.large_data[0] == 'A') {
    // Do something
  }

  return 0;
}
```

