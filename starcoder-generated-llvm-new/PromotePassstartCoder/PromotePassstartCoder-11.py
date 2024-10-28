
```c
#include <alloca.h>
#include <stdio.h>

// Define a function that uses stack-allocated variables
void example_function() {
  // Declare variables using alloca
  int a = alloca(sizeof(int)); // Declare and initialize a variable
  int b = alloca(sizeof(int)); // Declare and initialize another variable

  // Promote a to a register
  register int r = *a;

  // Perform nested operations on a and b, possibly allocating too much stack memory
  for (int i = 0; i < 10000; i++) {
    r = *a;
    for (int j = 0; j < 100; j++) {
      r += *b;
    }
  }

  // Print the results to ensure the variables are used
  printf("r: %d\n", r);
}

int main() {
  // Call the function
  example_function();
  return 0;
}
```

