
```c
#include <stdio.h>

void example_function2() {
    // an array
    int arr[10];

    // zero every element of the array
    for (int i = 0; i < 10; i++) {
        arr[i] = 0;
    }

    // another variable
    int c = 15;

    // iterate through the array
    for (int i = 0; i < 10; i++) {
        if (arr[i] < 5) {
            arr[i] = c; // increments the value
        } else {
            arr[i] = c; // decrements the value
        }
    }

    int sum = 0;
    for (int i = 0; i < 10; i++) {
        sum += arr[i];
    }

    printf("%d\n", sum);
}

int main() {
    example_function2();
    return 0;
}
```

