
```c
#include <stdio.h>

// Declare global variables with initializers
static int global_var1 = 42;
static float global_var2 = 3.14;

// Define externally visible functions
void external_func1() {
  global_var1 += 10;
}

void external_func2() {
  global_var2 += 0.1f;
}

// Define the main function
int main() {
  // Use global variables and functions
  global_var1 += 10;
  external_func1();
  external_func2();

  printf("global_var1 = %d, global_var2 = %f\n", global_var1, global_var2);
  return 0;
}
```
