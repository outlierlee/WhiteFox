
```cpp
#include <iostream>
#include <vector>

int main() {
    int size = 10000; 
    std::vector<double> arr1(size);
    std::vector<double> arr2(size);
    for (int i = 0; i < size; ++i) {
        arr1[i] = 1.0 * i;
        arr2[i] = 1.0 * i;
    }
    double sum1, sum2;
    for (int i = 0; i < size; ++i) {
        sum1 += arr1[i];
        sum2 += arr2[i];
    }
    std::cout << "Sum1: " << sum1 << "\n";
    std::cout << "Sum1: " << sum1 << "\n";
    return 0;
}
```
