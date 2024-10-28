
```c
#include <stdio.h>

// Result of function
int result1 = 0;
int result2 = 0;

// A Function to demonstrate example of common subexpression elimination using function calls.
int performOperation(int i) {
    int res = i * 32;
    res <<= 1; 
    return res;
}

int main() {

    // Declare variables and assign values
    int a = 5, b = 16, c = 5;

    // Original computations
    result1 = a * b;
    result2 = c * b;

    // Functions calls to operate with their result may fail elimination of common subexpression
    result1 = performOperation(result1);
    result2 = performOperation(result2);

    // Use the results - demonstration of benefit of CSE exists here
    printf("Result1: %d\n", result1);
    printf("Result2: %d\n", result2);

    return 0;
}
```

In C program, we can use Common Subexpression Elimination feature, but function calls inhibit the elimination. Therefore, the functions calls are put to highlight the requirement.