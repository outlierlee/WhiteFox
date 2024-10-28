
```c
static int global_var = 42;

static int use_global_var() {
 return global_var;
}

int main() {
    int result;
    result = use_global_var();
    return result; 
}
```

