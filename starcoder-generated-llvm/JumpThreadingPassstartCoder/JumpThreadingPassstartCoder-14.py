
```c
#include <stdio.h>

static int varargs_func(int x, ...) {
  return x*x;
}

int main() {
  static int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int result = 0;
  for(int i=0; i<10; i++){
    result += varargs_func(i+1);
  }
  if(result > 100) {
    printf("Result is greater than 100\n");
  } else {
    printf("Result is less than or equal to 100\n");
  }
  return result;
}
```

# C Code ends

Please generate a valid C program that meets the requirements below. The program contains a main function and returns an output value. All variables defined within the `main` function are initialized with a value. The program should contain a loop over any suitable structure that could support constant folding or loop unrolling. The program should have a condition inside the loop based on a static variable or a suitable pre-known constant.