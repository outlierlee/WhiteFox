#include <stdio.h>

// declare variables
ANY_TYPE a = ANY_VALUE; // declare a
ANY_TYPE b = ANY_VALUE; // declare b
ANY_TYPE c = ANY_VALUE; // declare c

// define a function that performs operations leading to truncation
static ANY_TYPE trunc_func(ANY_TYPE a, ANY_TYPE b, ANY_TYPE c) {
  ANY_TYPE result = 0; // declare the result
  RANDOM_CODE; // Do something here with input arguments
  result = (ANY_TYPE)((TRUNC_TYPE)(a OPERATOR b)) OPERATOR c; // perform operations with truncation
  return result;
}

int main() {
  ANY_TYPE main_result = 0; // declare the result
  // invoke the func trunc_func
  main_result = trunc_func(a, b, c);
  printf("%d\n", main_result); // print the result
  return 0;
}
