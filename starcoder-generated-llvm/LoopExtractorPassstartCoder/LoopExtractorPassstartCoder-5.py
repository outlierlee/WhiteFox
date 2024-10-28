
```c
#include <stdio.h>

// Define a function that contains a nested loop
void nested_loop_function(int x) {
  int i, j;
  int sum = 0; // Initialize a variable to accumulate results

  // A nested loop of two dimensions that iterates a random number of times in each dimension
  for (i = 0; i < x; i++) {
    for (j = 0; j < x; j++) {
      sum += i + j; // Accumulate the sum of the loop indices
    }
  }

  // Print the result to ensure the nested loops are not optimized away
  printf("Nested Sum: %d\n", sum);
}

int main() {
  // Call the function containing the nested loop
  nested_loop_function(10);

  return 0; // Return 0 to indicate successful execution
}
```

