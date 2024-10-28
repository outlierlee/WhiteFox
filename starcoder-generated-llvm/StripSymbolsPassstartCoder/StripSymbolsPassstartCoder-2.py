
```cpp
#include <iostream>
#include <vector>

typedef struct {
    int a;
    float b;
} MyStruct;

MyStruct globalVar = {213, 34.4};

void useStruct(MyStruct *s) {
    std::cout << "a: " << s->a << ", b: " << s->b << std::endl;
}

int main() {
    useStruct(&globalVar);
    return 0;
}
```

