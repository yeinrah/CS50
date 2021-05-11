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
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain exactly 26 characters\n");
        return 1;
    }
    else
    {
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            for (int j = i + 1; j < strlen(argv[1]); j++)
            {
                if (argv[1][j] == argv[1][i])
                {
                    printf("Key must not contain repeated characters\n");
                    return 1;
                }
            }

            if (isalpha(argv[1][i]) == 0)
            {
                printf("Key must be alphabets\n");
                return 1;
            }
        }
    }

    //get key value
    string k = argv[1];

    //prompt the user for the plaintext
    string pt = get_string("plaintext: ");

    //compute the actual process
    string alphabet = "abcdefghijklmnopqrstuvwxyz";

    printf("ciphertext: ");

    for (int i = 0; i < strlen(pt); i++)
    {
        if (isalpha(pt[i]))
        {
            if (isupper(pt[i]))
            {
                for (int j = 0; j < strlen(alphabet); j++)
                {
                    if (pt[i] == toupper(alphabet[j]))
                    {
                        printf("%c", toupper(k[j]));
                    }
                }
            }
            else
            {
                for (int j = 0; j < strlen(alphabet); j++)
                {
                    if (pt[i] == (alphabet[j]))
                    {
                        printf("%c", tolower(k[j]));
                    }
                }
            }
        }
        else
        {
            printf("%c", pt[i]);
        }
    }

    printf("\n");
    return 0;
}