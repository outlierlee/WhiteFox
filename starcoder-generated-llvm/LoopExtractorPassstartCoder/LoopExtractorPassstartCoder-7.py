
```c
#include <stdio.h>
#define ITERATION_COUNT (5<<15)

// Define a function that contains a loop
void loop_function() {
  int i;
  int sum = 0; // Initialize a variable to accumulate results

  // A simple loop that iterates a fixed number of times
  for (i = 0; i < ITERATION_COUNT; i++) {
    sum += i; // Accumulate the sum of the loop index
  }

  // Print the result to ensure the loop is not optimized away
  printf("Sum: %d\n", sum);
}

int main() {
  // Call the function containing the loop
  loop_function();

  return 0; // Return 0 to indicate successful execution
}
```

