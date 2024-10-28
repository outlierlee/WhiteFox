
```c
#include <stdio.h>

#define N 5 // Define N

void example_function() {
    int a = N - 2; // Define a variable 'a'

    // Iterate for N times
    for(int i = 0; i < N; i++) {
        a += 1; // Increment 'a'
        printf("%d\n", a); // Output the value of 'a'
    }

    // Check a value
    if (a < N) {
        a = a + 5;
        printf("%d\n", a);
    } else {
        a = a - 3;
        printf("%d\n", a);
    }

    // Check a value again
    if (a < 10) {
        a = a + 1;
    } else {
        a = a - 2;
    }

    printf("%d\n", a); // Print a

    // Repeat the iterations
    for(int i = 0; i < N; i++) {
        a += 1; // Increment 'a'
        printf("%d\n", a); // Output the value of 'a'
    }
}

int main() {
    example_function(); // Call the function
    return 0;
}
```
