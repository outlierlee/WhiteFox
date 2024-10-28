
```c
#include <stdio.h>

int main() {
    int x = (1 << 31); // Declare a 32 bit variable
    int i; // Declare a loop counter variable
    int sum = 0; // Initialize a variable for the sum

    // A simple loop with a variable loop counter and a large induction variable
    for (i = x - 10; i < x + 10; i++) {
        sum += i; // Add the loop counter to the sum in each iteration
    }

    printf("Sum: %d\n", sum); // Print the result
    return 0;
}
```

