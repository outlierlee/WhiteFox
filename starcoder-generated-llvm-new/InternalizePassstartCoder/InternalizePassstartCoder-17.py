
```c
// Declare global variables with initializers
static int global_var3 = 42;
int internal_int = 42;
const int const_int = 42;
extern int extern_int;

// Define functions
static void internal_func1() {
  internal_int = internal_int + 1;
}

int main() {
  // Function body
  global_var3 += 10;
  internal_func1();
  return const_int;
}
```
