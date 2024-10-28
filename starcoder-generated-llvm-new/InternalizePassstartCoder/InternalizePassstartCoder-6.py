
```c
// Declare global variables with initializers
int global_var1 = 42;
float global_var2 = 3.14;

void external_func1() {
  global_var1 += 10;
  global_var2 /= 2.0;
}

void external_func2() {
  global_var1 -= 5;
  global_var2 *= 3.14;
}

// Define the main function
int main() {
  // Use global variables and functions
  global_var1 += 10;
  external_func1();
  external_func2();
  return global_var1; // Return value depends on global variables
}
```

