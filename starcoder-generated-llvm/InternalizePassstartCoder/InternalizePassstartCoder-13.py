
```c
#include <stdio.h>
#include <string.h>

// Declare global variables with initializers
int global_var1 = 42;
float global_var2 = 3.14;

// Define functions
void external_func1() {
  global_var1 += 1;
  printf("Inside external function 1\n");
}

void external_func2() {
  global_var2 -= 0.1;
  printf("Inside external function 2\n");
}

// Define the main function
int main() {
  // Use global variables and functions
  global_var1 += 10;
  global_var2 -= 1.0;
  external_func1();
  external_func2();
  printf("Inside main function\n");
  return 0;
}
```

