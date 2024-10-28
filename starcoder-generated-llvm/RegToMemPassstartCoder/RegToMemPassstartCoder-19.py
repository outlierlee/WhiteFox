```c
#include <stdio.h>

// Define a function that uses local variables
void example_function() {
  // Declare multiple local variables
  int a = 10;
  float b = 20.5;
  char c = 'c';
  double d = 2.95085085724;
  unsigned int ui = 1234567890;

  // Perform some operations using these variables
  a += 5;
  b *= 2.0;
  c = 'd';

  // Print the results
  printf("a: %d, b: %f, c: %c, d: %lf, ui: %u\n", a, b, c, d, ui);
}

int main() {
  // Call the function
  example_function();

  return 0;
}
```
