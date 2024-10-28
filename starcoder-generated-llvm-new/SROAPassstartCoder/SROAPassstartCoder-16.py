
```cpp
#include <stdio.h>

// Define two arrays and a function to modify them
void modifyArrays(int arr1[], int arr2[]) {
    // Modify the arrays
    arr1[5] = 15;
    arr2[5] = 25;
}

int main() {
    // Define two arrays
    int arr1[10];
    int arr2[10];

    // Call the function to modify the arrays
    int arr3[10] = {0, 1, 2, 3, 4};
    modifyArrays(arr1, arr2, arr3[5]);

    // Print the arrays for demonstration purposes
    printf("arr1: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", arr1[i]);
    }
    printf("\n");

    printf("arr2: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", arr2[i]);
    }
    printf("\n");

    return 0;
}
```

