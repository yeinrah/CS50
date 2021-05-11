#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //validate user's input
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            if (isdigit(argv[1][i]) == 0)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
    }

    //get key value
    int k = atoi(argv[1]);

    //prompt the user for the plaintext
    string pt = get_string("plaintext: ");

    //compute the actual process
    for (int i = 0; i < strlen(pt); i++)
    {
        if (isalpha(pt[i]))
        {
            if (isupper(pt[i]))
            {
                pt[i] = (pt[i] - 'A' + k) % 26 + 'A';
            }
            else
            {
                pt[i] = (pt[i] - 'a' + k) % 26 + 'a';
            }
        }
    }
    printf("ciphertext: %s\n", pt);
}