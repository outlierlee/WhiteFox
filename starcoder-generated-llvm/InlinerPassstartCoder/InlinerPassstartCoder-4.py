
```cpp
#include <stdio.h>

static inline int simple_function(int a, int b) {
    return a * b; // Simple operation that can be easily inlined
}

int main() {
    int x = 5; // Declare and initialize variable x
    int y = 10; // Declare and initialize variable y
    int result; // Declare a variable to store the result

    // Call the simple_function with x and y as arguments
    result = simple_function(x, y);

    // Return the result of the function call
    return result;
}
```

