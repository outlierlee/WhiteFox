
```c
#include <string.h> // Include the necessary header for memcpy

// Define a struct or a large data type
typedef struct {
  char data[1000]; // Define a data array of any size
} LargeData;

int main() {
  LargeData source, destination; // Declare source and destination variables

  // Initialize the source with some values
  memset(&source, 'A', sizeof(LargeData));

  // Use memcpy to copy data from source to destination
  memcpy(&destination, &source, sizeof(LargeData));

  // Perform some operations on the destination to ensure it is used
  if (destination.data[0] == 'A') {
    // Do something
  }

  return 0;
}
```

