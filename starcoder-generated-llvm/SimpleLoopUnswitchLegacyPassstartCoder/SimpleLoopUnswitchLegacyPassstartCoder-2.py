
```c
#include <stdio.h>

void loop_with_condition(int n, int flag) {
    for (int i = 0; i < n; ++i) {
        if (i % 2) { // This condition could be invariant depending on how we build the loop
            // Perform some operations
            printf("Iteration %d is odd\n", i);
        } else {
            // Perform some other operations
            printf("Iteration %d is even\n", i);
        }
    }
}

int main() {
    int n = 10; // Loop iteration count
    int flag = 1; // Invariant condition for the loop

    // Call the function with the loop
    loop_with_condition(n, flag);

    return 0;
}
```

