#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    else
    {
        FILE *file = fopen(argv[1], "r");

        if (file == NULL)
        {
            printf("Error : Invalid File\n");
            return 1;
        }

        BYTE buffer[512];
        int counter = 0;
        FILE *img_start = NULL;
        char filename[8];

        while (fread(&buffer, 512, 1, file) == 1)
        {
            if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
            {
                if (counter != 0)
                {
                    fclose(img_start);
                }

                sprintf(filename, "%03i.jpg", counter);
                img_start = fopen(filename, "w");
                counter++;
            }

            if (counter != 0)
            {
                fwrite(&buffer, 512, 1, img_start);
            }
        }

        fclose(file);
        fclose(img_start);
    }
}