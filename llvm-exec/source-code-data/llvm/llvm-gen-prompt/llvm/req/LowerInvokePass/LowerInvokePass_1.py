#include <setjmp.h>
#include <stdio.h>

// Declare a global jmp_buf variable
jmp_buf buf;

// Define a function that uses setjmp and longjmp
void test_function() {
  if (setjmp(buf)) {
    // Code to execute after longjmp
    printf("After longjmp\n");
  } else {
    // Code to execute before longjmp
    printf("Before longjmp\n");
    longjmp(buf, 1); // Trigger a jump back to the setjmp point
  }
}

int main() {
  // Call the function that uses setjmp and longjmp
  test_function();
  return 0;
}
