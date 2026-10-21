using System.Numerics;

public struct BigFloat
{
    public BigInteger Value;
    public static readonly BigInteger ScaleFactor = BigInteger.Pow(10, 300);

    public BigFloat(double val)
    {
        Value = (BigInteger)(val * 1_000_000_000_000.0) * (ScaleFactor / 1_000_000_000_000); // хотел запариться, получилось хД
    }

    public BigFloat(BigInteger val) { Value = val; }

    public static BigFloat operator *(BigFloat a, double b)
    {
        BigInteger b_scaled = (BigInteger)(b * 1_000_000_000.0);
        return new BigFloat((a.Value * b_scaled) / 1_000_000_000);
    }

    public double ToDouble()
    {
        if (Value == 0) return 0.0;

        return (double)Value / (double)ScaleFactor;
    }
}