
```cpp
#include <string.h>
#define ANY_SIZE 1024
#define ANY_VALUE 0x5F

typedef struct {
  char data[ANY_SIZE];
} LargeData;

int main() {
  LargeData source, destination;
  memset(&source, ANY_VALUE, sizeof(LargeData));
  memcpy(&destination, &source, sizeof(LargeData));
  if (destination.data[0] == ANY_VALUE) {
    // do something
  }
  return 0;
}
```
