
```cpp
#include<iostream>
#include<vector>
#include<string>

void loop_function() {
    int i;
    int sum = 0;

    std::vector<int> vec(10000);
    for (int i = 0; i < 10000; i++) {
      vec[i] = i + 2;
      sum += vec[i];
    }
    
    if (sum == 100010000) {
      sum = 100000000;
    }

    std::cout << "Sum: " << sum << std::endl;
}

int main() {
    loop_function();
    return 0;
}
```

