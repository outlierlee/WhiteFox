
```c
#include <stdio.h>

int main() {
    int x = 10; // declare and initialize x
    int y = 6; // declare and initialize y

    // A loop with a condition constant-folded
    while (x < 16) {
        // Perform some operation like bit-shift left with 2
        x = x << 2; // x is updated with a left bit-shift operation equivalent to x * 4
    }

    return x; // return the result
}
```

