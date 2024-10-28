
```cpp
#include <stdio.h>
#include <alloca.h>

// Define a function that uses stack-allocated variables
void example_function(int size) {
  int result;
  // Use the stack-allocated variable as an intermediate result
  result = 0; // Initialize the result variable
  for (int i = size-1; i >= 0; i--) { // Iterate from size to 0
    for (int j = 0; j < size; j++) { // Iterate from 0 to size
      // Use an array-like access element directly to use memory more efficiently
      int* array = (int*)alloca(size * sizeof(int)); // Allocate some memory
      // Use the array such that it might be promoted to a register
      array[i] = array[j] + 1; // Perform an operation using the array
    }
    // Update the result based on the array
    result += array[i]; // Add the array element to the result
  }
  // Print the intermediate result again to ensure the whole computation is preserved
  printf("Result: %d\n", result); // Print the result
}

int main() {
  int size = 100; // Declare the size variable
  // Call the function
  example_function(size);
  return 0;
}
```

