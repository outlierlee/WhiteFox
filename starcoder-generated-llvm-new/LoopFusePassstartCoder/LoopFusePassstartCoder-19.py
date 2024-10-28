
```cpp
#include <iostream>
#include <vector>
#include <thread>

static void operation(int *array, int start, int end) {
    for (int i = start; i < end; i++) {
        array[i] *=2;
    }
}

int main() {
    int result = 0;
    int array1[10];
    std::vector<int> vec = {0, 1, 2, 3, 4};

    // Initialize arrays
    for(int i = 0; i < 10; i++) {
        array1[i] = i * 2;
    }

    // Create two threads
    std::thread t1(operation, array1, 0, 5);
    std::thread t2(operation, array1, 5, 10);

    // Wait for the threads to finish
    t1.join();
    t2.join();

    // Print the results
    for(int i = 0; i < 10; i++) {
        result += array1[i];
    }
    
    std::cout << result << "\n";
    
    return 0;
}
```
