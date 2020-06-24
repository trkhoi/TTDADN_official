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
        public async Task controlDeviceStart()
        {
            string t1 = timeStart.Text, d = device.Text;
            //int on = 1, off = 0;
            //int intensity = 100;
            string script_on = "python publisher.py --on 1 --bright 255";
            //handle start time for device
            var startTime = t1;
            var timeParts1 = startTime.Split(new char[1] { ':' });
            
            var dateNow = DateTime.Now;
            var dateStart = new DateTime(dateNow.Year, dateNow.Month, dateNow.Day,
                       int.Parse(timeParts1[0]), int.Parse(timeParts1[1]), int.Parse(timeParts1[2]));
            TimeSpan ts1;
            if (dateStart > dateNow)
            {
                ts1 = dateStart - dateNow;
            }
            else
            {
                dateStart = dateStart.AddDays(1);
                ts1 = dateStart - dateNow;
            }
            await Task.Delay(ts1).ContinueWith((x) => run_cmd_publisher(script_on));
        }
        public async Task controlDeviceEnd()
        {
            string t2 = timeEnd.Text, d = device.Text;
            //int on = 1, off = 0;
            //int intensity = 100;
            string script_off = "python publisher.py --on 0 --bright 0";
            //handle start time for device
            var endTime = t2;
            var timeParts2 = endTime.Split(new char[1] { ':' });

            var dateNow = DateTime.Now;
            //handle end time for device
            var dateEnd = new DateTime(dateNow.Year, dateNow.Month, dateNow.Day,
                       int.Parse(timeParts2[0]), int.Parse(timeParts2[1]), int.Parse(timeParts2[2]));
            TimeSpan ts2;
            if (dateEnd > dateNow)
            {
                ts2 = dateEnd - dateNow;
            }
            else
            {
                dateEnd = dateEnd.AddDays(1);
                ts2 = dateEnd - dateNow;
            }
            await Task.Delay(ts2).ContinueWith((x) => run_cmd_publisher(script_off));
        }
        //static public string script = "python publisher.py --on 1 --bright 255";
        public static void run_cmd_publisher(string script)
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
            controlDeviceStart();
            controlDeviceEnd();
            //MessageBox.Show("a");
        }
    }
}
