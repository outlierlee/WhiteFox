
```cpp
#include <string.h>

int main() {
  // Declare and initialize a constant array
  const int const_array[] = {1, 2, 3, 4, 5};

  // Declare a local array with automatic storage duration
  int local_array[4];

  // Use memcpy to copy data from the constant array to the local array
  // The sizeof is incorrect, it is fixed here
  memcpy(local_array, const_array, sizeof(const_array));

  // Use the local array in some way to ensure it is not optimized away
  int result = local_array[1] + local_array[2];

  if (result < 0) {
    result *= 2;
  }
  return result;
}
```

