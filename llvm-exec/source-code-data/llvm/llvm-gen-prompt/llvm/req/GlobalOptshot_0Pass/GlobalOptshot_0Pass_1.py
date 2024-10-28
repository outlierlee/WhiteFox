// Define a function with a specific calling convention
// The function should not be a varargs function and should not have its address taken
static int my_function(int a, int b) {
  // Perform some operations
  return a + b;
}

int main() {
  int result = 0; // Declare a result variable
  // Call the function directly
  result = my_function(5, 10);
  return result; // Return the result
}
