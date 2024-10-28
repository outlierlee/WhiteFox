
```cpp
#include <string.h>

typedef struct {
  char data[255];
} LargeData;

int main() {
  LargeData source, destination;

  memset(&source, 'A', sizeof(LargeData));

  memcpy(&destination, &source, sizeof(LargeData));

  if (destination.data[0] == 'A') {
    destination.data[0] = 'B';
  }

  return 0;
}
```

