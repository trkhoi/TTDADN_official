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
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace TTDADN
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        static public string disk = "D:";
        static public string path = "D:\\Material Design\\python_scripts";
        static public string script = "python main.py";
        public static void run_cmd_subscriber()
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
            process.StandardInput.WriteLine(script);
            //process.StandardInput.WriteLine(script);
            process.StandardInput.Flush();
            process.StandardInput.Close();
            //process.WaitForExit();
            
        }
        public MainWindow()
        {
            run_cmd_subscriber();
            InitializeComponent();
        }
    }
}
