
```cpp
// declare a global variable with an initial constant value of 10
static int global_var = 10;

// define a function that uses the global variable
static int use_global_var() {
  return global_var; // return the global variable
}

int main() {
  int result = 0; // declare a result variable
  // call the function that uses the global variable
  result = use_global_var();
  return result; // return the result
}
```

