
```c
#include <stdio.h>

// A function with a loop containing a condition
void loop_with_condition(int n, int flag) {
    for (int i = 0; i < n; ++i) {
        switch(flag)
        {
        case 0:
            // Perform some operations when flag is false
            printf("Flag is false, iteration %d\n", i);
            flag = 1;
            break;
        default:
            // Perform some operations when flag is true
            printf("Flag is true, iteration %d\n", i);
            flag = 0;
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

