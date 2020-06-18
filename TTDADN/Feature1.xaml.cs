using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;
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
    /// Interaction logic for Feature1.xaml
    /// </summary>
    /// 
    public class Parameter : INotifyPropertyChanged
    {
        private int _temperature;

        public int Temperature
        {
            get { return _temperature; }
            set { _temperature = value; OnPropertyChanged(); }
        }

        private int _light;

        public int Light
        {
            get { return _light; }
            set { _light = value; OnPropertyChanged(); }
        }

        private int _humidity;

        public int Humidity
        {
            get { return _humidity; }
            set { _humidity = value; OnPropertyChanged(); }
        }


        public event PropertyChangedEventHandler PropertyChanged;
        protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }

    public partial class Feature1 : Window, INotifyPropertyChanged
    {
        private Parameter _param;

        public Parameter Param
        {
            get { return _param; }
            set { _param = value; OnPropertyChanged(); }
        }


        public Feature1()
        {
            InitializeComponent();
            this.DataContext = this;
            CreateFileWatcher("D:\\Projects\\C#\\TTDADN_official\\TTDADN\\bin\\Debug\\");
        }

        public void CreateFileWatcher(string path)
        {
            FileSystemWatcher watcher = new FileSystemWatcher();
            watcher.Path = path;

            watcher.NotifyFilter = NotifyFilters.LastAccess | NotifyFilters.LastWrite | NotifyFilters.FileName |
                NotifyFilters.DirectoryName;
            watcher.Filter = "*.json";

            watcher.Changed += new FileSystemEventHandler(OnChanged);
            watcher.Created += new FileSystemEventHandler(OnChanged);
            watcher.Deleted += new FileSystemEventHandler(OnChanged);
            watcher.Renamed += new RenamedEventHandler(OnRenamed);

            watcher.EnableRaisingEvents = true;
        }

        private void OnChanged(object source, FileSystemEventArgs e)
        {
            System.Threading.Thread.Sleep(1000);
            var jsonString = File.ReadAllText("D:\\Projects\\C#\\TTDADN_official\\TTDADN\\bin\\Debug\\demo.json");
            Param = JsonConvert.DeserializeObject<Parameter>(jsonString);
        }

        private static void OnRenamed(object source, RenamedEventArgs e)
        {

        }

        public event PropertyChangedEventHandler PropertyChanged;
        protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            var jsonString = File.ReadAllText("D:\\Projects\\C#\\TTDADN_official\\TTDADN\\bin\\Debug\\demo.json");
            Param = JsonConvert.DeserializeObject<Parameter>(jsonString);
        }

    }
}
