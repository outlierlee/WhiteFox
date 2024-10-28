
```cpp
#include <cstring>

typedef struct {
  char data[1024 * 1024]; // Define a data array of 1MB size
} LargeData;

int main() {
  LargeData source, destination;

  // Initialize the source with some values
  memset(&source, 0xA5, sizeof(LargeData));

  // Use memcpy to copy data from source to destination
  memcpy(&destination, &source, sizeof(LargeData));

  // Perform some operations on the destination to ensure it is used
  if (destination.data[0] == 0xA5) {
    destination.data[0] = 'A'; // causes the data array use optimizations.
  }

  return 0;
}
```
