#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //prompt the user for their card number
    long n;
    do
    {
        n = get_long("Number: ");
    }
    while (n < 0);

    int digit = 0;
    int checksum = 0;

    while(n > 9)
    {
        int i = 0;
        i = n % 10;
        n = (n - i) / 10;
        digit++;
    }

    //calculate checksum
    for (int i = 0; i < (digit / 2); i++)
    {
        int r1 = 0;
        int r2 = 0;

        r1 = n % 10;
        n = (n - r1) / 10;
        checksum += r1;

        if (n < 10)
        {
            checksum += n;
            break;
        }

        r2 = n % 10;
        n = (n - r2) / 10;

        if (r2 > 4)
        {
            int r3 = 0;
            r3 = (r2 * 2) % 10;
            r2 = (r2 * 2 - r3) / 10;
            checksum = checksum + r2 + r3;
        }
        else
        {
            checksum += r2 * 2;
        }

        if (n < 10)
        {
            checksum += n;
            break;
        }
    }

    if (checksum % 10 != 0)
    {
        printf("INVALID\n");
        return 1;
    }
    else
    {
        //determine if the number is valid or not
        if (digit != 13 && digit != 15 && digit != 16)
        {
            printf("INVALID\n");
            return 1;
        }
        else
        {
            //determine starting digit
            int modulo(int n, int digitNum)
            {
                int i = 0;
                for (int k = 0; k < digitNum; k++)
                {
                    if (n < 10)
                    {
                        break;
                        return n;
                    }
                    i = n % 10;
                    n = (n - i) / 10;
                }
                return i;
            }

            //determine company
            if (digit == 15 && modulo(n, 15) == 3 && modulo(n, 15) ==37)
            {
                printf("AMEX\n");
            }
            else if (digit == 16 && modulo(n, 15) == 51,52,53,54,55)
            {
                printf("MASTERCARD\n");
            }
            else if (digit == 13 || digit == 16 && modulo(n, 13) == 4 || modulo(n, 16) == 4)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
                return 1;
            }
        }
    }
}