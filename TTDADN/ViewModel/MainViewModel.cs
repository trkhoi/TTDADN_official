using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using Test.viewmodel;

namespace TTDADN.ViewModel
{
    public class MainViewModel : BaseViewModel
    {
        public bool isLoaded = false;
        public ICommand LoadedWindowCommand { get; set; }
        public ICommand command_1 { get; set; }
        //public ICommand command_2 { get; set; }
        public ICommand command_3 { get; set; }
        public ICommand command_4 { get; set; }
        public ICommand command_5 { get; set; }


        // mọi thứ xử lý sẽ nằm trong này
        public MainViewModel()
        {
            LoadedWindowCommand = new RelayCommand<object>((p) => { return true; }, (p) => {
                isLoaded = true;
                LoginWindow loginWindow = new LoginWindow();
                loginWindow.ShowDialog();
            }
              );
            command_1 = new RelayCommand<object>((p) => { return true; }, (p) => { Feature1 wd = new Feature1(); wd.ShowDialog(); });
            //command_2 = new RelayCommand<object>((p) => { return true; }, (p) => { Feature2 wd = new Feature2(); wd.ShowDialog(); });
            command_3 = new RelayCommand<object>((p) => { return true; }, (p) => { Feature3 wd = new Feature3(); wd.ShowDialog(); });
            command_4 = new RelayCommand<object>((p) => { return true; }, (p) => { Feature4 wd = new Feature4(); wd.ShowDialog(); });
            command_5 = new RelayCommand<object>((p) => { return true; }, (p) => { Feature5 wd = new Feature5(); wd.ShowDialog(); });

            //if (!isLoaded)
            //{
            //    isLoaded = true;
            //    LoginWindow loginWindow = new LoginWindow();
            //    loginWindow.ShowDialog();
            //}


        }
    }
}
