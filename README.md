# pi-LCD-temperature
First experiment for using Raspberry Pi and Arduino together;
I use an LCD connected to the arduino which accepts  CPU TEMP inputs from the Raspberry Pi through USB Serial.
The arduino then decodes the inputs and outputs them to the display through the LiquidCrystal library.

**Wiring**

![Wiring](https://www.arduino.cc/en/uploads/Tutorial/LCD_Base_bb_Fritz.png)

**Autostart**

You can automate the script using CRONTAB.
To edit the crontab, you just type:

crontab -e

If asked, choose nano as your editor.
Scroll to the bottom of the file and add this single line:
@reboot python3 /home/pi/temp_monitor.py
This assumes that your script is called temp_monitor.py and that it’s saved in your home directory.
