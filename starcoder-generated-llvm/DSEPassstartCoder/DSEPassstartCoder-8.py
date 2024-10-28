
```cpp
int main() {
    std::string str = {"It's 2AM and we've just got this. What time is it? It's 3AM...THE MORNING IS ALREADY HERE..."};
    int a[2];
    int* ptr1 = a;
    int* ptr2 = (int*)malloc(100 * sizeof(int));
    if (!ptr2) return -1;
    memset(ptr2, 5, 100 * sizeof(int));

    // Pointer arithmetic and dereferencing
    *(ptr1 + 100) = 10;
    *ptr2 = 11;
    free(ptr2);
  
    return str.size();
}
```

