
```cpp
#include<iostream>
using namespace std;

void F1(int* array) {
    int i;
    for(i =0; i<10; i++)
        array[i]+=1;
}

void F2(int* array) {
    int i;
    for(i =0; i<10; i++)
        array[i]+=2;
}

int main()
{
    int i, array1[10], array2[10];

    for(i = 0; i < 10; i++) {
        array1[i] = i;
        array2[i] = i * 2;
    }

    F1(array1);
    F2(array2);

    for(i=0; i<10; i++)
        cout << array1[i] + array2[i] << " ";

    return 0;
}
```

