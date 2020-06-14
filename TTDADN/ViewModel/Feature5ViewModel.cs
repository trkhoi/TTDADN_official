using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using Test.viewmodel;

namespace TTDADN.ViewModel
{
    public class Feature5ViewModel : BaseViewModel
    {
        public ICommand ShowCommand { get; set; }
        public Feature5ViewModel()
        {
            ShowCommand = new RelayCommand<object>((p) => { return true; }, (p) => { propStat wd = new propStat(); wd.ShowDialog(); });
        }
    }
}
