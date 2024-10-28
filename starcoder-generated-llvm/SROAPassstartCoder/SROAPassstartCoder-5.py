
```cpp
#include <iostream>
#include <vector>
#include <array>
#include <bitset>
#include <limits>
#include <cfloat>
#include <algorithm>

// Define a struct with multiple fields
struct MyStruct {
    int a;
    float b;
    char c;
};

// Function that uses the struct
void useStruct(MyStruct* s) {
    // Perform operations on the struct fields
    s->a = -10;
    s->b = 30.7;
    s->c = 'p';
}

int main() {
    // Declare a struct variable
    MyStruct s;

    // Call the function that uses the struct
    useStruct(&s);

    if (s.a == -10 && s.b == 30.7 && s.c == 'p') {
        // Format string
        printf("%d %f %c\n", s.a, s.b, s.c);
    }

    return 0;
}
```
