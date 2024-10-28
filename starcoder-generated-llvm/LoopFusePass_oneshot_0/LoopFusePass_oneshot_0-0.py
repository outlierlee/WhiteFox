
```cpp
#include <vector>
#include <numeric>
using namespace std;

int main() {
    int array1[10];
    int array2[10];

    for (int i = 0; i < 10; i++) {
        array1[i] = i * 2;
    }

    for (int i = 0; i < 10; i++) {
        array2[i] = array1[i] + 1;
    }
    
    return 0;
}
```

