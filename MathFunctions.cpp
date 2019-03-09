/**
 * power - calculate the power of number
 * @param base: Base value
 * @param exponent: Exponent value.
 * @return base raised to the power exponenet
 * 
**/
//#include "MathFunctions.h"
double power(double base, int exponent)
{
    int result = base;
    int i;
    if (exponent == 0){
        return 1;
    }
    for (i=1; i<exponent; i++){
        result *= base;
    }
    return result;
}