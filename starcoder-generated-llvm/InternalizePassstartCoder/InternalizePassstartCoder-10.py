
```c
// Declare global variables with initializers
static int global_var1 = 42; // declared as extern and static on gcc but treated as static (since it's before main)
float global_var2 = 3.14;

// Define functions
static void external_func1() {} // marked as extern and static on gcc but treated as static (since it's before main)
static void external_func2() {} // both extern and static on gcc but treated as static (since it's before main)

// Define the main function
int main() {
  // Use global variables and functions
  global_var1 += 10;
  external_func1();
  external_func2();
  return 0; // return is 0 = SUCCESS
}
```
