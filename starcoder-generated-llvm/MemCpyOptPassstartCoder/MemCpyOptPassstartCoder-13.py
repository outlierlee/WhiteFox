
```c
#include <string.h>

typedef struct {
  char data[1000];
} LargeData;

int main() {
  LargeData source, destination;

  memset(&source, 'A', sizeof(LargeData));

  memcpy(&destination, &source, sizeof(LargeData));

  if (destination.data[0] == 'A') {
    // Do something
  }

  return 0;
}
```

