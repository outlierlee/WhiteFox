
```c
#include <stdio.h>

#define N 5 // arbitrary size
int arr[N][N];

int main() {
    int i, j, sum = 0;

    // initialization of arr[][]
    for(i = 0; i < N; i++) {
        for(j = 0; j < N; j++) {
            arr[i][j] = (i*10 + j) * 10;
        }
    }

    // Computing and updating sum
    for(i = 0; i < N; i++) {
        for(j = 0; j < N; j++) {
            sum += (arr[i][j] % 2 == 0)? arr[i][j] : 0; 
        }
    }

    return sum;
}
```

