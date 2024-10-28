
```cpp
#include <string>

// define a function with any calling convention except fastcc. This function should not be a varargs function and should not have its address taken.
void __attribute__((noinline)) func(std::string arg1, int arg2, double arg3) {
    // Do something here with input arguments
}

int main() {
    // declare some variables
    std::string x = "hello"; // declare variable x
    int y = 42; // declare variable y
    double z = 3.14;

    // invoke the func
    func(x, y, z); // you can pass the arguments with any number, any type

    return 0;
}
```

