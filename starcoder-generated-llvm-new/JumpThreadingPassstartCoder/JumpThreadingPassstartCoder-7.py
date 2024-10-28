
```c
#include <stdio.h>

// Define a function with a simple conditional structure
int simple_conditional(int a, int b) {
    if (a > 100) {
        return b + 32;
    } else {
        return b - 15;
    }
}

int main() {
    int x = 101; // Initialize variable x
    int y = 10; // Initialize variable y
    int result = 0; // Declare result variable

    // Call the function with a constant condition
    result = simple_conditional(x, y);

    // Use the result in a conditional branch
    if (result > 20) {
        printf("Result is greater than 20\n");
    } else {
        printf("Result is 20 or less\n");
    }

    return 0;
}
```
