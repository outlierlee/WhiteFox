
```c
#include <stdio.h>

int getNonZeroValue() {
    return 1; // or any other non-zero constant
}

int main() {
    int a = getNonZeroValue(); // Call the function to get a non-zero value
    int b = 0; // Initialize a variable to zero
    int isZero = 0;
    //  printf("Value of isZero = %d\n", isZero);
    for (int i = 0; i < 10; ++i) {
        if (i % 2 == 0) {
            b = i; // Assign the non-zero value to b
            // printf("Value of isZero = %d\n", isZero);
        } else {
            b = a; // Assign a non-zero value to b
            // printf("Value of isZero = %d\n", isZero);
        }

        // Compare the variable with zero
        if (b == 0) {
            printf("b is zero\n");
            isZero = 1;
            // printf("Value of isZero = %d\n", isZero);
        } else {
            printf("b is non-zero\n");
            if(isZero)
            {
                printf("This value of b doesn't match the non-static one, hence not optimized\n");
                isZero = 0;
            }
            // printf("Value of isZero = %d\n", isZero);
        }
    }

    return 0;
}
```
