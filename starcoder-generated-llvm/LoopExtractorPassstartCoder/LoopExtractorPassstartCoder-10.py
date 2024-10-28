
```c
#include <stdio.h>

// Function will be optmized.
void loop_function() {
	int i;
	int sum=0;

	//this small loop per element will cause some single-instruction loop transformations.
	for(i=0; i<10000000; i++) {
		sum += i;
	}

	printf("Sum: %d\n", sum);
}

int main() {
    loop_function();
	return 0;
}
```

