
```cpp
#include <iostream>
#include <vector>
#include <string>

typedef struct {
    int a;
    float b;
} MyStruct;

MyStruct globalVar = {1, 2.0};

void useStruct(MyStruct *s) {
    if (s->b > 2) {
        printf("b: %f\n", s->b);
    } else {
        printf("b: %f\n", s->b);
    }
}

int main() {
    useStruct(&globalVar);
    std::vector<MyStruct> vec;
    MyStruct temp = {0, 1};
    std::string str = "hello";
    vec.push_back(temp);
    temp.a = 2;
    useStruct(&vec[vec.size()]);
    
    for(char c : str) {
        if(c == 'h') {
            printf("Character found\n");
            break;
        }
    }
    
    return 0;
}
```
