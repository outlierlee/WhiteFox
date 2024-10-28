
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<int> array1(5), array2(5), array3(5);

    // Initialize arrays
    for (int i = 0; i < 5; i++) {
        array1.at(i) = i;
        array2.at(i) = 2*i;
    }

    // First loop: perform some operations on array1
    for (int &i : array1) {
        i++;
    }

    // Second loop: perform some operations on array2
    for (int &i : array2) {
        i += 2;
    }

    // Use the results of the loops
    for (int i = 0; i < 5; i++) {
        array3.at(i) = array1.at(i) + array2.at(i);
    }

    // Print the results
    for (int i : array3) {
        std::cout << i << " ";
    }

    return 0;
}
```
