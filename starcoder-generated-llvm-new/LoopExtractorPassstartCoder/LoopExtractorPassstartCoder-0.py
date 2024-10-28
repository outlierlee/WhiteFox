
```cpp
#include <vector>
#include <string>

class LoopExample {
public:
    void loop_func(int a, int b) {
      int sum = 0;
      for (int i = 0; i < 10; i++) {
          sum += a * b;
      }
      printf("Sum is %d\n", sum);
    }
};

int main() {
    LoopExample loop_example;
    loop_example.loop_func(2, 3);
    return 0;
}
```

