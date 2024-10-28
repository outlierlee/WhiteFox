
```c
#include <stdio.h>

int a = 1 << 31; // declare and initialize with left shift
int b = a; // declare and initialize b
volatile int c = 0;  // declare and initialize c
volatile int d = 0;  // declare and initialize d

// define a function that performs some operations
int compute(int x, int y) {
  int result = 0; // initialize
  __asm__ ("addl %1,%0" : "=r" (result) : "r" (x), "0" (y));
  return result; 
}

int main() {
  int main_result = 0; 
  volatile int z0, z1, z2 = c;
  volatile int v = 1;
  
  if (1) {
    for (int i = 0; i<16; i++){
      for (int j = 0; j<16; j++){
      c+=2;
      }
    }
  }

  for (int i = 0; i < 2; i++){
    z0++;
    z1++;
  }

  main_result = v;

  compute(main_result, a);

  printf("Result: %d\n", main_result);

  return 0; 
}
```
