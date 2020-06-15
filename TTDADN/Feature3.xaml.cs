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
using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace TTDADN
{
    /// <summary>
    /// Interaction logic for Feature3.xaml
    /// </summary>
    //public class Light
    //{
    //    public int lightValue;

    //    public int LightValue
    //    {
    //        get { return lightValue; }
    //        set { lightValue = value; } 
    //    }
    //}

    public class PublishParameter : INotifyPropertyChanged
    {
        private int _light;

        public int Light
        {
            get { return _light; }
            set { _light = value; OnPropertyChanged(); }
        }

        public event PropertyChangedEventHandler PropertyChanged;
        protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }

    }
    public partial class Feature3 : Window, INotifyPropertyChanged
    {
        private PublishParameter param;

        public event PropertyChangedEventHandler PropertyChanged;
        protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }

        public PublishParameter Param
        {
            get { return param; }
            set { param = value; OnPropertyChanged(); }
        }

        static public string script = "python publisher.py --topic \"abc\" --state ";
        public void run_cmd_publisher()
        {
            script += Param.Light.ToString();
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
            MessageBox.Show("Finished publishing temperature");
            //process.WaitForExit();

        }
        public Feature3()
        {
            InitializeComponent();
            this.DataContext = this;
            Param = new PublishParameter();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            run_cmd_publisher();
            Param.Light = 0;
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            Param.Light = 0;
            run_cmd_publisher();
        }
    }
}
