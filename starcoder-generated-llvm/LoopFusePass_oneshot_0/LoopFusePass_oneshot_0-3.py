
```cpp
#include <iostream>
using namespace std;

int main() {
    int array1[10], array2[10];
    int i;

    // First loop
    for(i=0; i<10; i++) {
        array1[i] = 2*i + 1; // Fill array1 with odd numbers
    }

    // Second loop
    for(i=0; i<10; i++) {
        array2[i] = 3*i;  // Fill array2 with multiples of 3
    }

    return 0;
}
```
