#include "renderer.h"

int main()
{
    char inputPath[256], outputPath[256];

    for (int i = 0; i < 100; i++)
    {
        sprintf(inputPath, "../frames/frame_%05d.bin", i);
        sprintf(outputPath, "../frames/frame_%05d.png", i);

        render_frame(inputPath, outputPath);
    }

    printf("Render finished. Press Enter to exit...");
    getchar();
    return 0;
}
