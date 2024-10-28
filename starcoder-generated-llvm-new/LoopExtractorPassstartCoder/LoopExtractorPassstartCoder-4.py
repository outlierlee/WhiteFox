
```c
#include <stdio.h>

// Define a function that contains a loop
void loop_function(enum { start, loop } state, int* arr, int size) {
  int i;
  int sum = 0; // Initialize a variable to accumulate results

  // A simple loop that iterates a fixed number of times
  for (i = start; i < size; i++) {
    sum += arr[i]; // Accumulate the sum of the loop index
  }

  // Print the result to ensure the loop is not optimized away
  printf("Sum: %d\n", sum);
}

int main() {
  int arr[10];
  for (int i = 0; i < 10; ++i) {
    arr[i] = i;
  }

  // Call the function containing the loop
  loop_function(start, arr, 10);

  return 0; // Return 0 to indicate successful execution
}
```
# C Code Ends

Please generate a valid C++ Code that meets the requirements below. The code should contain a `main` function. And the main function gives back an output value. Please initialize all the variables you define with a value. The code should be compilable and runnable without any errors. You are supposed to have undefined behavior in your code. This is a case of want you see is what you get :).