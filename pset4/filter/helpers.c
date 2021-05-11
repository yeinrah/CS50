#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;
            int gray = round((r + g + b) / 3.0);

            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtBlue = gray;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][width - j - 1];
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float temp_counter = 0;
            int temp_r = 0;
            int temp_g = 0;
            int temp_b = 0;

            for (int a = -1; a < 2; a++)
            {
                for (int b = -1; b < 2; b++)
                {
                    if (i + a >= 0 && j + b >= 0 && i + a < height && j + b < width)
                    {
                        temp_counter++;
                        temp_r += temp[i + a][j + b].rgbtRed;
                        temp_g += temp[i + a][j + b].rgbtGreen;
                        temp_b += temp[i + a][j + b].rgbtBlue;
                    }
                }
            }
            image[i][j].rgbtRed = round(temp_r / temp_counter);
            image[i][j].rgbtGreen = round(temp_g / temp_counter);
            image[i][j].rgbtBlue = round(temp_b / temp_counter);
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int xr = 0;
            int xg = 0;
            int xb = 0;
            int yr = 0;
            int yg = 0;
            int yb = 0;

            for (int a = -1; a < 2; a++)
            {
                for (int b = -1; b < 2; b++)
                {
                    if (i + a >= 0 && j + b >= 0 && i + a < height && j + b < width)
                    {
                        if (a == -1)
                        {
                            if (b == -1)
                            {
                                xr += (temp[i + a][j + b].rgbtRed) * -1;
                                yr += (temp[i + a][j + b].rgbtRed) * -1;
                                xg += (temp[i + a][j + b].rgbtGreen) * -1;
                                yg += (temp[i + a][j + b].rgbtGreen) * -1;
                                xb += (temp[i + a][j + b].rgbtBlue) * -1;
                                yb += (temp[i + a][j + b].rgbtBlue) * -1;
                            }
                            else if (b == 0)
                            {
                                xr += (temp[i + a][j + b].rgbtRed) * 0;
                                yr += (temp[i + a][j + b].rgbtRed) * -2;
                                xg += (temp[i + a][j + b].rgbtGreen) * 0;
                                yg += (temp[i + a][j + b].rgbtGreen) * -2;
                                xb += (temp[i + a][j + b].rgbtBlue) * 0;
                                yb += (temp[i + a][j + b].rgbtBlue) * -2;
                            }
                            else
                            {
                                xr += (temp[i + a][j + b].rgbtRed) * 1;
                                yr += (temp[i + a][j + b].rgbtRed) * -1;
                                xg += (temp[i + a][j + b].rgbtGreen) * 1;
                                yg += (temp[i + a][j + b].rgbtGreen) * -1;
                                xb += (temp[i + a][j + b].rgbtBlue) * 1;
                                yb += (temp[i + a][j + b].rgbtBlue) * -1;
                            }
                        }
                        else if (a == 0)
                        {
                            if (b == -1)
                            {
                                xr += (temp[i + a][j + b].rgbtRed) * -2;
                                yr += (temp[i + a][j + b].rgbtRed) * 0;
                                xg += (temp[i + a][j + b].rgbtGreen) * -2;
                                yg += (temp[i + a][j + b].rgbtGreen) * 0;
                                xb += (temp[i + a][j + b].rgbtBlue) * -2;
                                yb += (temp[i + a][j + b].rgbtBlue) * 0;
                            }
                            else if (b == 0)
                            {
                                xr += (temp[i + a][j + b].rgbtRed) * 0;
                                yr += (temp[i + a][j + b].rgbtRed) * 0;
                                xg += (temp[i + a][j + b].rgbtGreen) * 0;
                                yg += (temp[i + a][j + b].rgbtGreen) * 0;
                                xb += (temp[i + a][j + b].rgbtBlue) * 0;
                                yb += (temp[i + a][j + b].rgbtBlue) * 0;
                            }
                            else
                            {
                                xr += (temp[i + a][j + b].rgbtRed) * 2;
                                yr += (temp[i + a][j + b].rgbtRed) * 0;
                                xg += (temp[i + a][j + b].rgbtGreen) * 2;
                                yg += (temp[i + a][j + b].rgbtGreen) * 0;
                                xb += (temp[i + a][j + b].rgbtBlue) * 2;
                                yb += (temp[i + a][j + b].rgbtBlue) * 0;
                            }
                        }
                        else
                        {
                            if (b == -1)
                            {
                                xr += (temp[i + a][j + b].rgbtRed) * -1;
                                yr += (temp[i + a][j + b].rgbtRed) * 1;
                                xg += (temp[i + a][j + b].rgbtGreen) * -1;
                                yg += (temp[i + a][j + b].rgbtGreen) * 1;
                                xb += (temp[i + a][j + b].rgbtBlue) * -1;
                                yb += (temp[i + a][j + b].rgbtBlue) * 1;
                            }
                            else if (b == 0)
                            {
                                xr += (temp[i + a][j + b].rgbtRed) * 0;
                                yr += (temp[i + a][j + b].rgbtRed) * 2;
                                xg += (temp[i + a][j + b].rgbtGreen) * 0;
                                yg += (temp[i + a][j + b].rgbtGreen) * 2;
                                xb += (temp[i + a][j + b].rgbtBlue) * 0;
                                yb += (temp[i + a][j + b].rgbtBlue) * 2;
                            }
                            else
                            {
                                xr += (temp[i + a][j + b].rgbtRed) * 1;
                                yr += (temp[i + a][j + b].rgbtRed) * 1;
                                xg += (temp[i + a][j + b].rgbtGreen) * 1;
                                yg += (temp[i + a][j + b].rgbtGreen) * 1;
                                xb += (temp[i + a][j + b].rgbtBlue) * 1;
                                yb += (temp[i + a][j + b].rgbtBlue) * 1;
                            }
                        }
                    }
                }
            }
            float Gr = sqrt(xr * xr + yr * yr);
            if (Gr > 255)
            {
                Gr = 255;
            }
            float Gg = sqrt(xg * xg + yg * yg);
            if (Gg > 255)
            {
                Gg = 255;
            }
            float Gb = sqrt(xb * xb + yb * yb);
            if (Gb > 255)
            {
                Gb = 255;
            }
            image[i][j].rgbtRed = round(Gr);
            image[i][j].rgbtGreen = round(Gg);
            image[i][j].rgbtBlue = round(Gb);
        }
    }
}
