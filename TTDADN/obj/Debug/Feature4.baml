   M S B A M L   `   `   `  ����A  =TTDADN, Version=1.0.0.0, Culture=neutral, PublicKeyToken=nullclr-namespace:TTDADNTTDADN  5   	   =#clr-namespace:TTDADN.UserControlBarTTDADN.UserControlBar  5	   	       TTDADN.Feature4   5   	   W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   &localclr-namespace:TTDADN     5   	   2uc#clr-namespace:TTDADN.UserControlBar     5	   	   V RMaterialDesignThemes.Wpf, Version=3.1.1.1361, Culture=neutral, PublicKeyToken=nullFmaterialDesign1http://materialdesigninxaml.net/winfx/xaml/themes  5
   	      MaterialDesignBody#���   5   	   $��Regular"�5      $��13(�5      &   System.Windows.Media.TextOptions    TextFormattingMode$  Ideal=�5         TextRenderingMode$
 Auto=�5        MaterialDesignPaper#���  5        MaterialDesignFont#���  5       � 
ResizeMode$ NoResize=�5   	    � WindowStyle$
 None=�5   	    � Title$ Feature4��5   	   $	��450��6   $	��800��6'   .��5      �  � RowDefinitions 5   
   �� 5      $
��auto �6   6,   �� 5      $	��100 �6   6+   �� 5      $��80 �6   6*   �� 5      $	��150 �6   6+   �� 5      6   .+�5   
   � $��0��6   .+�5      &    TTDADN.UserControlBar.ControlBar  6   5       � 5!   
   $��1��6   .+�5"      �� $��Center=�5#      $��Center=�5$       $  MaterialDesignHeadline3TextBlock#��[ 5%      Setting Devices5'      5(      � 5)   
   $��2��6    � ColumnDefinitions 5*      �� 5+      6%   �� 5,      6%   �� 5-      6%   .+�5/      � $��0��6   $	��200��6#   .+�50      �� -   5         ��Name$ device��50      $��Choose device:��6,   $��25(�6B   $��0 25 0 0q�6P   6d   51      � 52      $��1��6   .+�53      �� $��50��6   )  #MaterialDesignThemes.Wpf.HintAssist   Hint$ Search��54      	   HintOpacity$		 .26Q�55      
 �� 
IsEditable
 . .@�57      �� .��6#   Light59      �� 5:      .��6#   	Speaker5<      5=      5>      5?      � 5@   
   $��3��6    5A      �� 5B      6"   �� 5C      6"   .+�5E      � $��0��6   .+�5F      �� $��Time Start: ��5G      $��35 0 0 0q�5H      $��Center=�5I      $
��Left=�5J      $��25(�5K      5L      �� 5M      -   5         ��Name$ 	timeStart��5N      $
 Time��5O      $	��100��5P      $��
266 0 10 0q�5Q       % !MaterialDesignFloatingHintTextBox#��[ 5R      $��Center=�5S      $
��Left=�5T      5U      � 5V      $��1��6   .+�5W      �� $��
Time End: ��5X      $��35 0 0 0q�5Y      $��Center=�5Z      $
��Left=�5[      $��25(�5\      5]      �� 5^      -   5        $ timeEnd��5_      $
 Time��5`      $	��100��5a      $��
266 0 10 0q�5b      #��[ 5c      $��Center=�5d      $
��Left=�5e      5f      5g      � 5h   
   $��4��6   .+�5i      � $��1��6   .+�5j      �� -   5        $	��200��5k       $  MaterialDesignFlatAccentBgButton#��[ 5l       � ToolTip$. (MaterialDesignFlatAccentBackgroundButton��5m      .��6Z   Set5o      5p      5q      5r      5s      