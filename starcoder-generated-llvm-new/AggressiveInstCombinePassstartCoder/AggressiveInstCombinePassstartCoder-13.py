
```c
#include <stdio.h>

char a = 'a'; // initializing variable
char b = 'b'; // initializing variable
char c = 'c'; // initializing variable

static char trunc_func(char a, char b, char c) {
  char result = 0; // declare the result
  result = (char)((char)(a + b)) & c; // perform operations with truncation
  return result; 
}

int main() {
  char main_result = 0; 
  // invoke the func trunc_func
  main_result = trunc_func(a, b, c);
  printf("%c\n", main_result); // print the result
  return 0;
}
```
# C program ends