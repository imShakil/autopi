# mousemovement
A python project based on tkinter module to manipulate auto mouse movement.
In case you need to keep up window active, you can use this application.
It will move mouse and press keyboard button to make window active.

# Pre-requirements
- `Pyautogui`
- `python3-tk`
- `python3-dev`
- `scrot`

# How to Install?

I already added all pre-requirements inside the python script. During running this script it will check all requirement packages. Incase it will install such pakcage those are missing in your linux distro.

So, First of all lets clone this repository:

```
git clone https://github.com/imShakil/autopi.git /opt/autopi
```

Now, let's move as super user:

```
sudo su -
```

It will ask the `root` user password.

Let's move into the directory.

```
cd /opt/autopi/bin
```

Now give permission to the binary file.

```
chmod +x autopi
```

Finally, run the application with following command:

```
./autopi
```

It will check and install the requirement processes.

# Overview

This is a pretty simple application with 3 buttons only to `start`, `stop` and `exit` the application.
It looks like:

![overview.png](/bin/overview.png)

# Create Desktop Entry

To run this application from dash menu, Create a desktop entry `mouse-movement.desktop` with the following text:

```
[Desktop Entry]
Version=1.0
Name=Auto Pi
Comment=AutoPi
Exec=/opt/autopi/bin/autopi
Icon=/opt/autopi/bin/icon.png
Terminal=false
Type=Application
Categories=Utility;Application;
StartupWMClass=MouseMovement
```

Put this desktop entry inside:

```
/usr/local/share/applications/
```
