
```c
#include <stdio.h>

// Define a function with a loop containing a condition
void loop_with_condition(int n, int flag) {
    for (int i = 0; i < n; ++i) {
        if (flag == 1) {
            printf("Flag is true, iteration %d\n", i);
        } else if (flag == 0) {
            printf("Flag is false, iteration %d\n", i);
        } else {
            printf("Flag is invalid, iteration %d\n", i);
        }
    }
}

int main() {
    int n = 15;
    int flag = 1; // Invariant condition for the loop

    // Call the function with the loop
    loop_with_condition(n, flag);

    return 0;
}
```

