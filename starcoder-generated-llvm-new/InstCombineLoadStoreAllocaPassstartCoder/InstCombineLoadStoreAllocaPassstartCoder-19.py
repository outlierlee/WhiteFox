
```cpp
#include <cstring>

int main() {
  // Declare and initialize a constant array
  const char const_array[] = "hello";

  // Declare a local array with automatic storage duration
  char local_array[7];

  // Use strcpy to copy data from the constant array to the local array
  strcpy(local_array, const_array);

  // Use the local array in some way to ensure it is not optimized away
  int result = 0;
  for (int i = 0; i < strlen(local_array); i++) {
    result += local_array[i];
  }

  return result;
}
```

