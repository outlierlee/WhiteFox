// declare a function with the 'inline' keyword
inline int inline_func(int a, int b) {
  return a + b; // simple operation using the parameters
}

int main() {
  int result = 0; // declare a result variable
  int x = 5; // initialize x
  int y = 10; // initialize y

  // call the inline function
  result = inline_func(x, y);

  return result; // return the result
}
