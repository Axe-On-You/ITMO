using System;
using System.Numerics; // Complex

public class Fractal
{
    public int Width { get; }
    public int Height { get; }

    public Fractal(int width, int height)
    {
        Width = width;
        Height = height;
    }

    public double[,] Generate(BigFloat cx, BigFloat cy, BigFloat scale)
    {
        double[,] result = new double[Height, Width];

        double dScale = scale.ToDouble();
        if (dScale == 0) dScale = 1e-300; // Заглушка, если double обнулился

        double dCx = cx.ToDouble();
        double dCy = cy.ToDouble();

        for (int y = 0; y < Height; y++)
        {
            double im = (y - Height / 2.0) * dScale + dCy;

            for (int x = 0; x < Width; x++)
            {
                double re = (x - Width / 2.0) * dScale + dCx;

                System.Numerics.Complex z = new System.Numerics.Complex(re, im);
                result[y, x] = IterateCollatz(z);
            }
        }

        return result;
    }

    // Комплексная функция Колладца
    // f(z) = 0.25 * (2 + 7z - (2 + 5z) * cos(pi * z))
    private double IterateCollatz(Complex z)
    {
        int maxIter = 255;
        for (int i = 0; i < maxIter; i++)
        {
            if (z.Magnitude > 100) return i;

            Complex cosPart = Complex.Cos(Math.PI * z);
            Complex nextZ = 0.25 * (2 + 7 * z - (2 + 5 * z) * cosPart);
            z = nextZ;
        }
        return maxIter;
    }
}