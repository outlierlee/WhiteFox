
```cpp
#include <string.h>
#define ANY_SIZE 6
#define ANY_VALUE 'a'

typedef struct {
  char data[ANY_SIZE];
} LargeData;

int main() {
  LargeData source, destination;

  // Initialize the source
  memset(&source, ANY_VALUE, sizeof(LargeData));

  // Use memcpy to copy data from source to destination
  memcpy(&destination, &source, sizeof(LargeData));

  // Perform operation on the destination to ensure it is used
  if (destination.data[0] == ANY_VALUE) {
    destination.data[0] = 'b';
  }

  return 0;
}
```

