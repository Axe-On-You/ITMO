#define _CRT_SECURE_NO_WARNINGS
#include "renderer.h"
#include <stdio.h>
#include <stdlib.h>
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

void render_frame(const char* path, const char* outputPath)
{
    FILE* file = fopen(path, "rb");
    if (!file) { printf("Failde to open %s\n", path); return; }

    int width, height;
    fread(&width, sizeof(int), 1, file);
    fread(&height, sizeof(int), 1, file);

    double* data = (double*)malloc(width * height * sizeof(double));
    fread(data, sizeof(double), width * height, file);
    fclose(file);

    // Конвертируем в 8-бит grayscale
    unsigned char* img = (unsigned char*)malloc(width * height);
    for (int i = 0; i < width * height; i++)
    {
        double v = data[i];
        if (v > 255) v = 255;
        img[i] = (unsigned char)v;
    }

    stbi_write_png(outputPath, width, height, 1, img, width);

    free(data);
    free(img);

    printf("Saved %s\n", outputPath);
}
