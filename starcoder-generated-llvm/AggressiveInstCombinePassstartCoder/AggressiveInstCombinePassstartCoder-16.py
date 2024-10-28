
```c
#include <stdio.h>

// declare variables
int a = 10; // declare a
int b = 5;  // declare b
int c = 100; // declare c

// define a function that performs operations leading to truncation
static int trunc_func(int a, int b, int c) {
  int result = 0;
  if (a > b) {
    result = a / b;
  } else if (b > a) {
    result = b / a;
  } else {
    result = a + b;
  }
  if (c % 15 == 0) {
    result *= c;
  } else if (c % 10 == 0){
    result *= c;
  } else {
    result += c;
  }
  return result;
}

int main() {
  int main_result = 0; 
  // invoke the func trunc_func
  main_result = trunc_func(a, b, c);
  printf("%d\n", main_result); // print the result
  return 0;
}
```
