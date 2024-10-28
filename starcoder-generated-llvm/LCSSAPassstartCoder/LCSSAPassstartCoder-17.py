
```c
#include <stdio.h>

// declare a function that operates on an array 
void func(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == 1) {
            arr[i] *= 2;
        } 
        else {
            if (arr[i] == 2) {
                arr[i] *= 3;
            }
        }
    }
}

int main() {
    int result = 0; 

    // declare and initialize an array
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    // call the function with the array
    func(arr, n);

    // loop through the array and calculate the result
    for (int i = 0; i < n; i++) {
        result += arr[i];
    }

    // print the result and return
    printf("Result is: %d\n", result);
    return result;
}
```

