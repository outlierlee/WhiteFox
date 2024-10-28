
```c
#include <stdio.h>

// Another function that contains variable arguments
void example_function(int a, int b, int c) {
    // Control flow that hijacks the order of the conditionals
    if (a < b) {
        a = a + 1; // increase a
    } else {
        c = c + 1; // increase c
        a = a + c; // increment both a and c
    }

    // Another conditional that can be optimized, but this one isn't very good
    if (a < b) {
        a = a + 1; // increase a again
    } else {
        c = c - 1; // decrease c
        a = a + c; // increment a and c
    }

    printf("%d\n", a); // Be careful to not eliminate this printf
}

int main() {
    example_function(10, 20, 30); // Call the function
    return 0;
}
```
