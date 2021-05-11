#include <stdio.h>

int modulo(int n, int digitNum)
{
    int i = 0;
    for (int k = 0; k < digitNum; k++)
    {
        i = n % 10;
        n = (n - i) / 10;
        if (n < 10)
        {
            return n;
        }
    }
    return i;
}

int main(void)
{
    printf(modulo(9835, 3));
}