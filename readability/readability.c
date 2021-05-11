#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    //prompt the user for the text
    string text = get_string("Text: ");

    //analyze the text
    float l = 0;
    //wordcount starts at 1, because I'm counting with space (1 space = 2 words)
    float w = 1;
    float s = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            l++;
        }
        else if (isspace(text[i]))
        {
            w++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            s++;
        }
    }

    //apply the Coleman-Liau formula
    float L = l / w * 100;
    float S = s / w * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    //print out the result
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 1 && index < 16)
    {
        printf("Grade %i\n", index);
    }
    else
    {
        printf("Grade 16+\n");
    }
}