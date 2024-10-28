```c
#include <stdio.h>

// Function With Inline
void example_function() {
    int b = 30;
    int a = 20;

    // Simple and Well-Defined Code Block
    if (a < b) {
        a = a + 1;
    } else {
        a = a - 1;
    }

    if (a > b) {
        a = a + 1;
    } else {
        a = a - 2;
    }

    //Use the variable to prevent dead code elimination
    printf("%d\n", a);
}

int main() {
    example_function(); // Call the function
    return 0;
}
```
