
```c
#include <string>

// Declare global variables with initializers
int global_var1 = 42;
float global_var2 = 3.14;

// Declare function prototypes
void external_func1();
void external_func2_();
std::string extern_string1;

// Define functions
void external_func1() {
  global_var1 += 1;
  extern_string1 = "A String";
}

void external_func2_() {
  global_var2 -= 1.0;
  extern_string1 += " and more";
}

// Define the main function
int main() {
  // Use global variables and functions
  global_var1 += 10;
  extern_string1 += " Appending Extra text";
  external_func1();
  external_func2_();
  return 0;
}
```
