
```cpp
#include <iostream>
#include <vector>
#include <string>

// Define a struct
struct MyStruct {
    int a;
    float b;
};

// Define a vector with the struct
std::vector<MyStruct> vecs = {{1, 2.0}};

// Define a function that uses the struct
void useStruct(MyStruct &s) {
    std::cout << "a: " << s.a << ", b: " << s.b << std::endl;
}

int main() {
    // Call the function with the struct from the vector
    useStruct(vecs[0]);
    return 0;
}
```

