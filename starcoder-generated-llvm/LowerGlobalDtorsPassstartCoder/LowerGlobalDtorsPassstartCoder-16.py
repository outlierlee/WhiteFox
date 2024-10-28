
```c
#include <stdio.h>

// Define a destructor function
void __attribute__((destructor)) my_destructor() {
    int a[10];
    int x = 0;
    for (int i = 0; i < 10; i++) {
        a[i] = x * x + x;
    }
    printf("Result: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

// Define another destructor function with a different priority
void __attribute__((destructor(101))) another_destructor() {
    int b[10];
    int y = 0;
    for (int i = 0; i < 10; i++) {
        b[i] = y * y - y;
    }
    printf("Result: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", b[i]);
    }
    printf("\n");
}

int main() {
    // RANDOM_CODE: Any code that does not affect the global destructors
    printf("Main function\n");
    return 0;
}
```

