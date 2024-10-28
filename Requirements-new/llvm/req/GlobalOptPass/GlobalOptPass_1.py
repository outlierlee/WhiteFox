// declare a function with a specific calling convention
static int my_function(int a, int b) {
  int result = 0; // declare the result
  RANDOM_CODE; // Do something here with input arguments
  result = a OPERATOR b; // result is related to a and b
  return result;
}

int main() {
  int x = ANY_VALUE; // declare x
  int y = ANY_VALUE; // declare y
  int main_result = 0; // declare the result

  // invoke the function my_function
  main_result = my_function(x, y);

  return main_result; // return the result
}
