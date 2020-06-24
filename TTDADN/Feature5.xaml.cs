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
    /// Interaction logic for Feature5.xaml
    /// </summary>
    public partial class Feature5 : Window
    {
        public static string a = "python getrp.py --mode ", b1 = "\"", b2 = "\" ", c = "--sensor ", d = "--day ", e1 = "--month ", f = "--year ", g = "--week ";
        public string path = "D:/Material Design/TTDADN_official/TTDADN/bin/Debug/", source = "";
        private void showFromResource(object sender, RoutedEventArgs e)
        {
            ImageWindow img = new ImageWindow();

            Uri resourceUri = new Uri(path + source, UriKind.Absolute);
            img.abc.Source = new BitmapImage(resourceUri);
            img.Show();
        }

        private void isClick(object sender, RoutedEventArgs e)
        {
            string day = "", week, month = "", year = "";
            string device = "", mode = "", rpScript = "", deviceUp = "", modeUp = "";
            string t = "_";
            if (((ComboBoxItem)Device.SelectedItem).Content.ToString() != null)
            {
                device = ((ComboBoxItem)Device.SelectedItem).Content.ToString();
            }
            deviceUp = UppercaseFirst(device);
            
            if ((bool)Day.IsChecked)
            {
                day = day1.Text;
                month = month1.Text;
                year = year1.Text;
                
                mode = Day.Content.ToString();
                modeUp = UppercaseFirst(mode);

                rpScript = a + b1 + mode + b2 + c + "\"" + device + "\"" + " " + d + day + " " + e1 + month + " " + f + year;
                source = deviceUp + t + modeUp + t + day + t + month + t + year + ".png";
            }
            else if ((bool)(Week.IsChecked))
            {
                week = week1.Text;
                year = year2.Text;

                mode = Week.Content.ToString();
                modeUp = UppercaseFirst(mode);

                rpScript = a + b1 + mode + b2 + c + "\"" + device + "\"" + " " + g + week + " " + f + year;
                source = deviceUp + t + modeUp + t + week + t + year + ".png";
            }
            else if ((bool)(Month.IsChecked))
            {
                month = month2.Text;
                year = year3.Text;

                mode = Month.Content.ToString();
                modeUp = UppercaseFirst(mode);

                rpScript = a + b1 + mode + b2 + c + "\"" + device + "\"" + " " + e1 + month + " " + f + year;
                source = deviceUp + t + modeUp + t + month + t + year + ".png";
            }
            run_cmd_getReport(rpScript);
            MessageBox.Show(source);
        }

        static string UppercaseFirst(string s)
        {
            if (string.IsNullOrEmpty(s))
            {
                return string.Empty;
            }
            char[] a = s.ToCharArray();
            a[0] = char.ToUpper(a[0]);
            return new string(a);
        }
        public static void run_cmd_getReport(string rpScript)
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
            process.StandardInput.WriteLine(rpScript);
            //process.StandardInput.WriteLine(script);
            process.StandardInput.Flush();
            process.StandardInput.Close();
            process.WaitForExit();

        }
        public Feature5()
        {
            InitializeComponent();
        }
    }
}
