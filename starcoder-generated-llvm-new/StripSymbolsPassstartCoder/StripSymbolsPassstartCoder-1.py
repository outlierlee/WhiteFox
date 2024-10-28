
```cpp
#include <iostream>

// Define a struct with a typedef
typedef struct {
    int a;
    double b;
} MyStruct;

// Define a global variable of the typedef struct
MyStruct globalVar = {1, 3.14159};

// Define a function that uses the typedef struct
void useStruct(MyStruct *s) {
    std::cout << "a: " << s->a << ", b: " << s->b << std::endl;
}

int main() {
    // Call the function with the global variable
    useStruct(&globalVar);
    return 0;
}
```

