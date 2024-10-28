
```cpp
#include <stdio.h>

// Define a function similar to the previous one
int simple_conditional(int a, int b) {
    if (a > 0) {
        return b + 1;
    } else {
        return b - 1;
    }
}

int main() {
    int x = 5; // Initialize variable x
    int y = 10; // Initialize variable y
    int result = 0; // Declare result variable

    // Call the function similar to the previous one
    result = simple_conditional(x, y);

    // Use the result similar to the previous example
    if (result > 10) {
        printf("Result is greater than 10\n");
    } else {
        printf("Result is 10 or less\n");
    }

    return result;
}
```

