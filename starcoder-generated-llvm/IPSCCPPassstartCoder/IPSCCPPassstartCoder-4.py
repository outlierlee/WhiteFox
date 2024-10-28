
```cpp
#include <string>
#include <vector>
#include <sstream>

static int global_var = 128; // An integer value

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
