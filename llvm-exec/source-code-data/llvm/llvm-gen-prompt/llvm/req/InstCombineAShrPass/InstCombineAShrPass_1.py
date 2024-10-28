#include <stdint.h>

int main() {
    // Declare variables
    int32_t x = ANY_VALUE; // Initialize x with any 32-bit integer value
    int32_t y = ANY_VALUE; // Initialize y with any 32-bit integer value
    int32_t result;

    // Perform a left shift with no signed wrap and then an arithmetic right shift
    result = (x << C1) >> C2; // C1 and C2 are constants such that C1 > C2

    // Return the result
    return result;
}
