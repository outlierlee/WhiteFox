
```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

typedef struct {
    int part1;
    int part2;
} _improved_pare;

_improved_pare func(_improved_pare pare) {
    _improved_pare ret_val;
    srand(time(NULL));
  
    ret_val.part1 = pare.part1 + rand() % 3;
    ret_val.part2 = pare.part2 - rand() % 3;

    return ret_val;
}

int main() {
    _improved_pare test_pare = {1, 2};
    _improved_pare ret_val = func(test_pare);
  
    std::cout << "Func1 returns: {" << ret_val.part1 << ", " << ret_val.part2 << "}\n";

    return 0;
}
```
