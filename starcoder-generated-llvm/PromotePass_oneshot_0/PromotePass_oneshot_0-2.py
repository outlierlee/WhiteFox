
```cpp
#include <vector>
#include <string>

int main() {
    int x = 1; // declare variable x
    int y = 2; // declare variable y
    int z = 3; // declare variable z

    int *p = new int; // allocate memory for an integer
    *p = x + y + z; // assign the sum of x, y, and z to the allocated memory

    int result = *p; // read the value from the allocated memory
    delete p; // deallocate the memory

    return result;
}
```

