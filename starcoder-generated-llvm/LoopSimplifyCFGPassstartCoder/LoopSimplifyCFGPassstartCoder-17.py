
```c
#include <stdio.h>

// Result of x modification can be any constant so this will run infinitely
int main() {
    int x = 0; // initialize x with a non-negative value
    int y = -1; // initialize y

    // A loop growing any positive integer to some big integer
    while (x < 1000000000) {
        // Perform a random operation on x to make it grow
        x = x + 100; // x will be never equal zero due to positive y
    }

    return x;  // Return nonsensical value as loop won't terminate
}
```
