
```cpp
#include <vector>
#include <string>
#include <stdlib.h>

// Define a struct with multiple fields
typedef struct MyStruct {
    int a;
    float b;
    char c;
} MyStruct;

// Function that uses the struct
void useStruct(MyStruct *s) {
    // Perform operations on the struct fields
    s->a = 10;
    s->b = 20.5;
    s->c = 'z';
}

int main() {
    // Declare a struct variable
    MyStruct s;
    std::vector<int> vec1 = {0, 1, 2, 3};
    std::string str = "hello";
    // Call the function that uses the struct
    useStruct(&s);
    str += s.c;
    vec1.push_back(5);
    printf("%d %f %c %s\n", s.a, s.b, s.c, str.c_str());

    // Print the struct fields
    return 0;
}
```
