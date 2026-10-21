using System;
using System.IO;

class Program
{
    static void Main()
    {
        string framesPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "..", "..", "..", "..", "frames");
        framesPath = Path.GetFullPath(framesPath);
        if (!Directory.Exists(framesPath)) Directory.CreateDirectory(framesPath);

        // Чем меньше разрешения, тем быстрее рендерится видео и создается кадр (kind of очев)
        int w = 1280;
        int h = 720;
        Fractal fractal = new Fractal(w, h);
        Camera cam = new Camera();

        cam.CenterX = new BigFloat(-1.0);
        cam.CenterY = new BigFloat(0.0);

        cam.Scale = new BigFloat(0.008333);

        int totalFrames = 100;

        for (int i = 0; i < totalFrames; i++)
        {
            double[,] frame = fractal.Generate(cam.CenterX, cam.CenterY, cam.Scale);

            for (int y = 0; y < h; y++)
            {
                for (int x = 0; x < w; x++)
                {
                    double iterations = frame[y, x];

                    double color;
                    if (iterations >= 250)
                    {
                        color = 0.0; // nig
                    }
                    else
                    {
                        color = (iterations % 20) * (255.0 / 20.0);
                    }

                    frame[y, x] = color;
                }
            }

            string file = Path.Combine(framesPath, $"frame_{i:D5}.bin");
            FrameWriter.WriteFrame(file, frame);

            cam.Zoom(0.95);
            Console.WriteLine($"Frame {i} | Scale: {cam.Scale.ToDouble():E2}");
        }

        Console.WriteLine("Done. Press key to exit.");
        Console.ReadKey();
    }
}