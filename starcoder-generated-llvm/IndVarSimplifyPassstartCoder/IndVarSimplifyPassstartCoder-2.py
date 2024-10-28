
```cpp
#include <stdio.h>

int main() {
    int sum = 0;                       // Initialize a sum variable
    unsigned int limit = 1UL << 31;    // Define a loop limit

    // A simple loop with an induction variable
    for (int i = 0; i < limit; i++) {
        sum += i;                     // Accumulate the sum of the induction variable
    }

    printf("Sum: %d\n", sum);         // Print the result
    return 0;
}
```
