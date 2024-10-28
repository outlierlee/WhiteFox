
```c
#include <stdio.h>
#include <string.h>

int func_with_unused_params(int a, int b, int c) {
  volatile char str[] = "Hello, world!"; // declare string
  int n = strlen(str); // find length of string
  int sum = 0; // declare sum
  for(int i = 0; i < n; i++){ // sum of ASCII values
    sum += (int)str[i];
  }
  // declare variables
  int x = 20;
  char y = 'A';
  char z = 'B';
  int result = x - y;
  return result;
}

int main() {
  int main_result = 0;
  main_result = func_with_unused_params(8, 16, 4);
  return main_result;
}
```
