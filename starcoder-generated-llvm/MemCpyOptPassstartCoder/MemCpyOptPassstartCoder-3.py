
```c
#include <string.h>

// Data is 1000 bytes large
#define ANY_SIZE 1000
#define ANY_VALUE 'A'

typedef struct {
  char data[ANY_SIZE];
} LargeData;

int main() {
  LargeData source, destination;

  memset(&source, ANY_VALUE, sizeof(LargeData));
  memcpy(&destination, &source, sizeof(LargeData));

  // The code above ensures the destination is used
  if (destination.data[ANY_SIZE - 1] == 'A') {
    // do something
  }

  return 0;
}
```
