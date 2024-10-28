
```c
#include<stdio.h>

static int my_function(int a, int b) __attribute__ ((stdcall));
int main() {
  int result = 0;
  result = my_function(5, 10);
  return result;
}

static int my_function(int a, int b) __attribute__ ((stdcall)) {
  return a + b;
}
```
To compile you can use 

`clang++ -std=c++14 -m32 -Wall hello.cpp -S -emit-llvm -o hello.ll`

and then see if there are any calls with the attribute `stdcall`, this means our optimization can not be done as the function is attribute marked as `stdcall` as part of its original declaration.

