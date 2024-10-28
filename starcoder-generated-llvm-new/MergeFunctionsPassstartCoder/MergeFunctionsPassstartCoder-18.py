
```cpp
#include <stdio.h>

static int func1(int a, int b) {
    int result = a + b;
    return result;
}

static int func2(int a, int b) {
    int result = a + b; // perform same operation as func1
    return result;
}

int main() {
    int x = 5, y = 10; // declare variables
    int result1 = func1(x, y); // Call the first function
    int result2 = func2(x, y); // Call the second function
    printf("Results: %d, %d\n", result1, result2); // Print the results
    return 0; // Return from main
}
```
