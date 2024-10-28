
```c
#include <stdio.h>

// Define a function with multiple complex conditional branches
void example_function() {
    int c = 15;
    int d = 25;
    int randVal1 = 5;
    int randVal2 = 10;
    int randVal3 = 15;
    if ((c < d) && (randVal1 < randVal2)) {
        for(int i = 0; i < 5; i++) {
            printf("%d\n", i);
        }
    }
    if ((c > d) && (randVal2 > randVal3)) {
       for(int i = 0; i < 10; i++) {
            printf("%d\n", i);
        }
    }
    if ((c < d) && (randVal1 < randVal2)) {
       for(int i = 0; i < 15; i++) {
            printf("%d\n", i);
        }
    }
    if ((c > d) || (randVal2 < randVal3)) {
       printf("%d\n", 1);
    }
}

int main() {
    example_function(); // Call the function
    return 0;
}
```
