
```c
#include <stdio.h>

static int opDispenser(int x, int y) { return x*y; }

static void loop1(int* x, int* y, int* z, int width) {
   int i;
   for (i = 0; i < width; i++) {
      x[i] = y[i] + z[i];
   }
}

static void loop2(int* x, int* y, int width) {
   int i;
   for (i = 0; i < width; i++) {
      y[i] += x[i];
   }
}

int main() {
    int array1[10], array2[10];
    
    // Initialize arrays
    for (int i = 0; i < 10; i++) {
        array1[i] = i;
        array2[i] = i * 2;
    }
    
    // Perform some operations
    loop1(array2, array1, array2, 10);
    loop2(array2, array1, 10);
    
    // Print the results
    for (int i = 0; i < 10; i++) {
        printf("%d ", array1[i]);
    }
    
    return 0;
}
```

