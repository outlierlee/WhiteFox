
```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

int main() {
    srand(static_cast<unsigned int>(time(0)));
    int a = 5, b = 2, c = 5;
    
    int result1 = 0, result2 = 0;
    for(int i = 0; i < 10; i++){
        int d = rand() % 100;        
        result1 += a + b * d + c / 5;     // First computation
        result2 += a + b * d + c / 5;     // Second computation, same as result1
    }
    
    std::cout << "Result1: " << result1 << std::endl;
    std::cout << "Result2: " << result2 << std::endl;

    return 0;
}
```

