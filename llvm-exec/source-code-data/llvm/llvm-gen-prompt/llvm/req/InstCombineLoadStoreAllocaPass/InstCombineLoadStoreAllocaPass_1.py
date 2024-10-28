#include <string.h>

int main() {
  // Declare and initialize a constant array
  const int const_array[] = {1, 2, 3, 4, 5};

  // Declare a local array with automatic storage duration
  int local_array[5];

  // Use memcpy to copy data from the constant array to the local array
  memcpy(local_array, const_array, sizeof(const_array));

  // Use the local array in some way to ensure it is not optimized away
  int result = local_array[0] + local_array[1];

  return result;
}
