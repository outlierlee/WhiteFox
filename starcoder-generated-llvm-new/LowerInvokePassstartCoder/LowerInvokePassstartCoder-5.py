
```cpp
#include <setjmp.h>
#include <stdio.h>

jmp_buf buf;

// Definition of a function inside the global environment
void function_test() {
  volatile int val = 10;
  if (setjmp(buf)) {
    printf("After longjmp inside function.\n");
  } else {
    printf("Before longjmp inside function.\n");
    val = val + 5;
    longjmp(buf, 1); // Jump back to the setjmp point
  }
}

int main() {
  // Call this function
  function_test(); // This should print "Before longjmp inside function." followed by "After longjmp inside function."
  return 0;
}
```
