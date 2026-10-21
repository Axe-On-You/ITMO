public class Camera
{
    public BigFloat CenterX { get; set; }
    public BigFloat CenterY { get; set; }
    public BigFloat Scale { get; set; }

    public Camera()
    {
        CenterX = new BigFloat(0.0);
        CenterY = new BigFloat(0.0);
        Scale = new BigFloat(0.05);
    }

    public void Zoom(double factor)
    {
        Scale = Scale * factor;
    }
}