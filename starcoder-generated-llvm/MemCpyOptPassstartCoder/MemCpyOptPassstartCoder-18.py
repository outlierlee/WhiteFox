
```cpp
#include<iostream>
#include<cstring>
using namespace std;

typedef struct {
    int data[10];
} LargeData;

int main() {
    LargeData source, destination;
    memset(&source, 0, sizeof(LargeData));
    source.data[0] = 20;
    memcpy(&destination, &source, sizeof(LargeData));
    destination.data[0] += 15;
    return destination.data[0];
}
```

