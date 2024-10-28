// declare variables
int x = ANY_VALUE; // declare x
ANY_TYPE y = ANY_VALUE; // declare y
ANY_TYPE z = ANY_VALUE; // declare z

// define a function with non-local linkage (not static) that has unused parameters
int func_with_unused_params(int a, int b, int c) {
  int result = 0; // declare the result
  RANDOM_CODE; // Do something here, but don't use the parameters a, b, or c
  result = x OPERATOR ANY_VALUE; // result is related to x
  return result;
}

int main() {
  int main_result = 0; // declare the result
  // invoke the func_with_unused_params
  // you can pass the arguments with any value, any type
  main_result = func_with_unused_params(x, y, z);
  return main_result; // return the result
}
