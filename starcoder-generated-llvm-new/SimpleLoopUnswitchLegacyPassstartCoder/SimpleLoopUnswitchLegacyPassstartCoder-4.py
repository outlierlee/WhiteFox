
```c
#include <stdio.h>

// Define a function with a loop containing a condition
void loop_with_condition(int n, int flag) {
    for (int i = 0; i < n; ++i) {
        if (flag) { 
            // Perform some operations
            printf("Flag is true, iteration %d\n", i);
        } else {
            // Perform some other operations
            printf("Flag is false, iteration %d\n", i);
        }
    }
}

int main() {
    int n = 10; 
    int flag = 1;

    loop_with_condition(n, flag);

    return 0;
}
```

