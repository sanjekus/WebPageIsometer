using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace ConsoleApplication1
{
    public class Site 
    {
        public string url;
        public float score;

    }
    class Program
    {
       


        static void Main(string[] args)
        {

            string[] files = Directory.GetFiles(@"C:\Users\santanu\Desktop\temp", "*.txt");
            foreach (string file in files)
            {
                string[] lines = System.IO.File.ReadAllLines(file);
                foreach (string line in lines)
                {
                    if (line.Contains("Url"))
                    {
                        
                        using (StreamWriter tw = File.AppendText(file+"Result.txt"))
                        {
                            tw.WriteLine(line);

                        }

                    }
                }
            }
            
           
        }
    }
}
