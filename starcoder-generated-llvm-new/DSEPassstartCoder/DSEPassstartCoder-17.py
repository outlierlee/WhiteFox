
```c++
#include <iostream>
using namespace std;

int main() { 
    int* ptr = new int;
    if (!ptr) return -1;

    *ptr = 10;

    *ptr = 20;

    delete ptr;

    return 0;
} 
```
