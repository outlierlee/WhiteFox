
```c
#include <stdio.h>

// Annotate this function using __attribute__(( always_inline ))
__attribute__(( always_inline ))
void loop_with_condition(int n, int flag) {
    for (int i = 0; i < n; ++i) {
        if (flag) { // This condition should be invariant within the loop
            // Perform some operations involving flag and i
            printf("Flag is true, iteration %d\n", i);
        } else {
            // Perform some other operations involving flag and i
            printf("Flag is false, iteration %d\n", i);
        }
    }
}

// Annotate this call using __attribute__(( always_inline ))
__attribute__(( always_inline ))
int main() {
    int n = 10; // Loop iteration count
    int flag = 1; // Invariant condition for the loop

    // Call the function with the loop
    loop_with_condition(n, flag);

    return 0;
}
```

