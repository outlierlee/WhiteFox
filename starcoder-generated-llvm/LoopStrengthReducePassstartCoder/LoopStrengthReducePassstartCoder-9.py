
```c
#include <stdio.h>

int main() {
    int sum = 0; // Initialize a variable to accumulate the sum
    
    // A brace-enclosed loop with a linear induction variable
    {
        int i; // Loop counter

        // Loop begin
        for (i = 0; i < 10; i++) {
            sum += i; // Accumulate the sum of the loop counter
        }
    }

    printf("Sum: %d\n", sum); // Print the result
    return sum;
}
```

