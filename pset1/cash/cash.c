#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    //ask the user how much change is owed
    float c;
    do
    {
        c = get_float("How much change do you need?: ");
    }
    while (c < 0);

    //round up the change
    c = round(c * 100);

    //count up to change
    int n = 0;

    while (0 < c)
    {
        if (25 <= c)
        {
            c -= 25;
            n++;
        }
        else if (10 <= c)
        {
            c -= 10;
            n++;
        }
        else if (5 <= c)
        {
            c -= 5;
            n++;
        }
        else if (1 <= c)
        {
            c -= 1;
            n++;
        }
    }

    printf("%i\n", n);
}