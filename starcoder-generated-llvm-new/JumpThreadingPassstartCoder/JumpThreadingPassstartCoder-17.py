
```c
#include <stdio.h>

// Define a function with a simple conditional structure 
int simple_conditional(int a, int b) {
    if (a % 3) {
        return b * 2;
    } else {
        return b / 2;
    }
}

int main() {
    int x = 10; // Initialize variable x
    int y = 15; // Initialize variable y
    int result = 0; // Declare result variable

    // Call the function with a constant condition 
    result = simple_conditional(x, y);

    if (result >= 20) {
        printf("Result is greater than or equal to 20\n");
    } else {
        printf("Result is less than 20\n");
    }

    return result;
}
```

