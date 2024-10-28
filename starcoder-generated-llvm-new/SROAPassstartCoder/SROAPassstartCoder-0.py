
```cpp
#include <iostream>

// Define a struct with multiple fields
struct MyStruct {
    int a;
    double b;
    char c;
    struct {
        int d;
        float e;
        long long f;
    } inner;
    MyStruct *pointer;
};

// Function that assigns values to the struct's fields
void initStruct(MyStruct *s) {
    s->a = 10;
    s->b = 20.5;
    s->c = 'z';
    s->inner.d = 30;
    s->inner.e = 40.5;
    s->inner.f = 50LL;
    MyStruct * nested_struct = new MyStruct;
    nested_struct->a = 100;
    nested_struct->b = 200.5;
    nested_struct->c = 'w';
    s->pointer = nested_struct;
}

int main() {
    // Declare a struct variable
    MyStruct s;

    // Call the function that initialises the struct
    initStruct(&s);

    // Print out the fields of the struct
    std::cout << s.a << " " << s.b << " " << s.c << " " << s.inner.d << " " << s.inner.e << " " << s.inner.f << std::endl;
    std::cout << s.pointer->a << " " << s.pointer->b << " " << s.pointer->c << std::endl;

    if (s.inner.d + s.inner.e > 0 || s.pointer->a > s.a) {
        // Use the fields in a way that potentially enables optimization
        MyStruct::inner nested;
        nested = s.inner;
        std::cout << "Optimization check: " << nested.d + nested.e << std::endl;
    }

    return 0;
}
```

