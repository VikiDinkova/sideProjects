using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Dobule");
            double a = 1.0;
            double b = 3000.01;
            double c = 3.0;
            double d = Math.Sqrt(b * b - 4.0 * a * c);
            double x1 = (-b + d) / 2.0 * a;
            double x2 = (-b - d) / 2.0 * a;
            Console.WriteLine("x1 = " + x1);
            Console.WriteLine("x1 = " + x2);

            Console.WriteLine("Float");
            float m = 1.0f;
            float n = 3000.01f;
            float p = 3.0f;
            double d2 = Convert.ToDouble(n * n + 4.0f * m * p);
            float df = Convert.ToSingle(Math.Sqrt(d2));
            float xf1 = (-n + df) / 2.0f * m;
            float xf2 = (-n - df) / 2.0f * m;
            Console.WriteLine("x1 = " + xf1);
            Console.WriteLine("x1 = " + xf2);
        }
    }
}
