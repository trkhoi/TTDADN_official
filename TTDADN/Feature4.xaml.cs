using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace TTDADN
{
    /// <summary>
    /// Interaction logic for Feature4.xaml
    /// </summary>
    public partial class Feature4 : Window
    {
        public async Task controlDevice()
        {
            string t1 = timeStart.Text, t2 = timeEnd.Text, d = device.Text;
            //int on = 1, off = 0;
            //int intensity = 100;

            var DailyTime = t1;
            var timeParts = DailyTime.Split(new char[1] { ':' });

            var dateNow = DateTime.Now;
            var date = new DateTime(dateNow.Year, dateNow.Month, dateNow.Day,
                       int.Parse(timeParts[0]), int.Parse(timeParts[1]), int.Parse(timeParts[2]));
            TimeSpan ts;
            if (date > dateNow)
            {
                ts = date - dateNow;
            }
            else
            {
                date = date.AddDays(1);
                ts = date - dateNow;
            }
            await Task.Delay(ts).ContinueWith((x) => run_cmd_publisher());
        }
        static public string script = "python publisher.py --on 1 --bright 255";
        public static void run_cmd_publisher()
        {
            Process process = new Process();
            process.StartInfo.FileName = "cmd.exe";
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.RedirectStandardInput = true;
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.UseShellExecute = false;
            process.Start();

            /*process.StandardInput.WriteLine(disk);
            process.StandardInput.Flush();
            process.StandardInput.WriteLine(path);
            process.StandardInput.Flush();*/
            //process.StandardInput.WriteLine(script);
            process.StandardInput.WriteLine(script);
            process.StandardInput.Flush();
            process.StandardInput.Close();
            //process.WaitForExit();

        }
        public Feature4()
        {
            //run_cmd_publisher();
            InitializeComponent();
        }

        private void set_Click(object sender, RoutedEventArgs e)
        {
            controlDevice();
            //MessageBox.Show("a");
        }
    }
}
