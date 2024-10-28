
```cpp
int main(){
    int x = 20; // declare variable x
    int y = 30; // declare variable y
    int z = 40; // declare variable z

    int *p = new int; // allocate memory for an integer
    *p = ((x + y + z) << 1); // assign the sum of x, y and z to the allocated memory and multiply by 2

    int result = *p; // read the value from the allocated memory
    delete p; // deallocate the memory

    return result;
}
```

