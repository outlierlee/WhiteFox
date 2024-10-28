
```c
#include <stdio.h>

// Define a function with multiple local variables
void local_variables_func() {
  // Declare multiple local variables
  int v1 = 10;
  long long v2 = 118111610342853867ull;
  double v3 = 5.0;
  char *v4 = "char_pointer";

  // Perform some operations using these variables
  v1 += 5;
  v2 *= 2;
  v3 = v3 / v3;

  // Print the results
  printf("v1: %d\n", v1);
  printf("v2: %lld\n", v2);
  printf("v3: %.10f\n", v3);
  printf("v4: %s\n", v4);
}

int main() {
  // Call the function
  local_variables_func();

  return 0;
}
```
