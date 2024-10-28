
```cpp
// Declare and initialize global variables
int global_var1 = 42;
float global_var2 = 3.14;

// Define an external function
void external_func1() {
  // Function body
  global_var1 += 40;
}

// Define an external function
void external_func2() {
  // Function body
  global_var2 *= 2.0;
}

// Define the main function
int main() {
  // Use global variables and functions
  global_var1 += 10;
  external_func1();
  external_func2();
  return 0;
}
```

