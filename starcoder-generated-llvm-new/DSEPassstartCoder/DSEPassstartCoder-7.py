
```c++
#include<iostream>
#define SIZE 40
using namespace std;

int main()
{
    int arr[SIZE] = {0};  // Initialize array elements as 0
    int *parr = arr; // Pointer to array

    for (int i = 0; i < SIZE; i++)  // assign simple integer array
    {
        arr[i] = i;
        cout << "arr[" << i << "] = " << arr[i] << "\n";
    }
    delete parr; // Delete array using pointer
    
    return 0;
}
```

