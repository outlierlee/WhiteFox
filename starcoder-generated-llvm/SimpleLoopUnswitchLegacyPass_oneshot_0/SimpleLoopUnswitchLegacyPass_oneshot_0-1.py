
```cpp
static bool const_condition(int i) {
   return i != 0;
}

void loop_func(int x) {
	for (int i = 0; i < x; ++i) {
		if (const_condition(i)) {
			i += 5;
		}
	}
}

int main() {
	int x = 10;
    loop_func(x);
    return 0;
}
```

