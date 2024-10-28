
```cpp
// Declare global constants
const float PI = 3.14159;
const int SEED = 1;

// Define external functions
static inline int internal_func1() {
  return SEED + 1;
}

static inline int internal_func2() {
  return SEED + PI;
}

// Define the main function
int main() {
  // Use global constants and functions
  int result = 0;
  result += internal_func1();
  result += internal_func2();
  return result;
}
```
