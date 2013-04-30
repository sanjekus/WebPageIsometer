using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.IO;
using System.Diagnostics;
using System.Text.RegularExpressions;

namespace WebPgeSim.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            //List<SelectListItem> selectOptions = new List<SelectListItem>();
            //string[] files = Directory.GetFiles(@"C:\Users\santanu\Desktop\temp", "*.txt");
            //foreach (string fileName in files)
            //{
            //    if (fileName.Contains("Result"))
            //    {
            //        string[] lines = System.IO.File.ReadAllLines(fileName);
            //        foreach (string line in lines)
            //        {
            //            string lineTrimmed = line.Trim();
            //            string url = lineTrimmed.Split(':')[1];
            //            url= Regex.Replace(url, @"[^\w\.@-]", "",RegexOptions.None);
            //            SelectListItem sli = new SelectListItem();

            //            sli.Text = url;
            //            sli.Value = url;

            //            selectOptions.Add(sli);
                             
            //        }
            //    }
            //}
            //ViewBag.SelectOptions = selectOptions;
            return View();
        }

        /*private void OutputHandler(object sendingProcess, DataReceivedEventArgs outLine)
        {
            if (outLine.Data != null)
                Console.Out.WriteLine(outLine.Data.ToString());
        }*/

        [HttpPost]
        public  ActionResult GetSim()
        {
            Process notePad = new Process();
            notePad.StartInfo.FileName = "C:\\Python27\\Python.exe";
            notePad.StartInfo.Arguments = "C:\\Users\\sanjekus\\workspace\\webiso\\Source\\Entry.py";
            //notePad.StartInfo.CreateNoWindow = true;
            //notePad.StartInfo.UseShellExecute = false;
            //notePad.StartInfo.RedirectStandardOutput = true;
            //notePad.OutputDataReceived += new DataReceivedEventHandler(OutputHandler);
            

            notePad.Start();
            notePad.WaitForExit();
            
                  
            //for (int i = 0; i < 5; i++)
            //{
            //    System.Threading.Thread.Sleep(10000);
            //}
            string url1, url2;
            double contentSimScore, visualSimScore, linkSimScore, structuralSimScore, totalSimScore = 0.0;
            string[] lines = System.IO.File.ReadAllLines(@"C:\Users\sanjekus\Desktop\sanjeev.txt");
            string URL = System.IO.File.ReadAllLines(@"C:\Users\sanjekus\workspace\webiso\Resources\TestSet\userURL.txt")[0];
            url1 = URL.Split('|')[0];
            url2 = URL.Split('|')[1];
            contentSimScore = System.Convert.ToDouble(lines[0]);
            linkSimScore = System.Convert.ToDouble(lines[1]);
            visualSimScore = System.Convert.ToDouble(lines[2]);
            structuralSimScore = System.Convert.ToDouble(lines[3]);
            totalSimScore = System.Convert.ToDouble(lines[4]);

            ViewData["contentSimScore"] = contentSimScore;
            ViewData["visualSimScore"] = visualSimScore;
            ViewData["linkSimScore"] = linkSimScore;
            ViewData["structuralSimScore"] = structuralSimScore;
            ViewData["totalSim"] = totalSimScore;
            ViewData["url1"] = url1;
            ViewData["url1"] = url2;


            return View();
        }

        [HttpPost]
        public ActionResult HandleForm(string URL1, string URL2)
        {
            System.IO.File.WriteAllText(@"C:\Users\sanjekus\workspace\webiso\Resources\TestSet\userURL.txt", URL1 + "|" + URL2);
            ViewData["URL1"] ="Submitted URL 1 : " + URL1;
            ViewData["URL2"] = "Submitted URL 2 : " + URL2;
                  
            return View("Index");
        }


        public ActionResult About()
        {
            return View();
        }
    }
}
