
```cpp
#include <array>
#include <vector>
#include <string>

int main() {
    int result = 0;

    int a = 10; 
    int b = 20; 
    int c = 30; 

    std::array<int, 10> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    for (int i = 0; i < 10; i++) {
        if (a < b && a < arr[i]) {
            result += a + arr[i];
        } else {
            result += b - arr[i];
        }
    }

    if (result > c) {
        printf("Result is greater than c\n");
    } else {
        printf("Result is less than or equal to c\n");
    }

    return result;
}
```

