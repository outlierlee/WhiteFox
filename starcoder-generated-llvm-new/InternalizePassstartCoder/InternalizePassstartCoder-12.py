```c
// Definitions
int global_var1 = 42;
float global_var2 = 3.14;
static int local_var = 100;

static void internal_func1() {
  global_var1 += 15;
  local_var *= 2;
}

static void internal_func2() {
  // Function body
}

// Main
int main() {
  // Function calls
  global_var1 += 10;
  internal_func1();
  internal_func2();
  return 0;
}
```
