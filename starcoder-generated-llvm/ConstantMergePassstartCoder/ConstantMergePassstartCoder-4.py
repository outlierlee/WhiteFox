
```cpp
#include <stdio.h>

static const int global1 = 42;
static const int global2 = 42; // Same value as global1

static const int global3 = 42; // Same value as global2
static const int global4 = 42; // Same value as global3
static const int global5 = -1; // Different from global1, global3, global4 and global2

static const int global6 = 6;
static const int global7 = 0; // Identical to the previous one
static const int global8 = 0; // Identical to the previous one

// Define a function that uses these global constants
int use_globals() {
    return global1 + global2 + global3 + global4 + global5;
}

int main() {
    int result = use_globals();
    printf("Result: %d\n", result);
    return 0;
}
```

