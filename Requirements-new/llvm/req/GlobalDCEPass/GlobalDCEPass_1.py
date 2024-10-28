// declare a static function that is never called
static int unused_function() {
  int result = 0; // declare a result variable
  RANDOM_CODE; // Do something here, but ensure the function is never called
  return result;
}

int main() {
  int main_result = 0; // declare the result
  // main function does not call unused_function
  RANDOM_CODE; // Do something here, but do not call unused_function
  return main_result; // return the result
}
