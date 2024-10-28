
```c
#include <stdio.h>

// Define a function that contains a loop within a loop
void nested_loop_function() {
  int i, j;
  int sum = 0; // Initialize a variable to accumulate results

  // Loops that iterate nested loops
  for (i = 0; i < 5; i++) {
    for (j = 0; j < 10; j++) {
      sum += i * j; // Accumulate the product of the loop indices
    }
  }

  // Print the result to ensure the loop is not optimized away
  printf("Sum: %d\n", sum);
}

int main() {
  // Call the function containing the nested loop
  nested_loop_function();

  return 0; // Return 0 to indicate successful execution
}
```

