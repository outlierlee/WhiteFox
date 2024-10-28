
```cpp
#include <cstring> // Include the necessary header for memcpy

// Define a struct or a large data type
struct LargeData {
  char data[1000]; // Define a data array of any size
};

int main() {
  LargeData source, destination; // Declare source and destination variables

  // Initialize the source with some values
  memset(&source, 1, sizeof(LargeData));

  // Use memcpy to copy data from source to destination
  memcpy(&destination, &source, sizeof(LargeData));

  // Perform some operations on the destination to ensure it is used
  if (destination.data[0] == 1) {
    // Do something
  }

  return 0;
}
```

