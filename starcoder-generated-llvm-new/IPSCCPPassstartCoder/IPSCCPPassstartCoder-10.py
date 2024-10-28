
```c
// declare a global variable with a constant value
static int global_var = 10; // an initial constant value

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

