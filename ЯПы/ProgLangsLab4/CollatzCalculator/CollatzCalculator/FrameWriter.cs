using System.IO;

public class FrameWriter
{
    // Запись кадра в бинарный файл
    public static void WriteFrame(string path, double[,] data)
    {
        int height = data.GetLength(0);
        int width = data.GetLength(1);

        using (var fs = new FileStream(path, FileMode.Create))
        using (var bw = new BinaryWriter(fs))
        {
            bw.Write(width);
            bw.Write(height);
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    bw.Write(data[y, x]);
                }
            }
        }
    }
}
