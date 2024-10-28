
```c
#include <string.h>

int main() {
  // Variant of this program will also work
  const int const_array[5] = {30, 87, 69, 28, 1};

  // Declare a local array with automatic storage duration
  int local_array[5];

  // Use memcpy to copy data from the constant array to the local array
  memcpy(local_array, const_array, sizeof(const_array));

  // Use the local array in some way to ensure it is not optimized away
  int result = local_array[0] - local_array[4];

  return result;
}
```

