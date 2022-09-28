#!/usr/bin/env python3


import os
import sys
import __main__

import PySide2.QtCore     as qtc
import PySide2.QtUiTools  as qtut


def resource_path(relative_path):
    """Return path of a resource file

    This is needed for programs "compiled" with pyinstaller with the
    --onefile option.  When running the program normally the required
    files (e.g. mydialog.ui) are located in a location relative to the
    the script.  But when running an .exe generated by pyinstaller the
    required files are unpacked into a temporary directory.

    This function determines if the script is being run normally or if
    is is a pyinstaller generated exectuble and will return the
    correct path for the requried files.

    """
    default_dir = os.path.dirname(os.path.abspath(__main__.__file__))
    mei_dir     = getattr(sys, '_MEIPASS', default_dir)
    return os.path.join(mei_dir, relative_path)


def load_ui(ui_fname, custom_widgets = None):
    """Create a Qt Window from a .ui file.

    Keyword Parameters
      ui_fname       -- Name of the user interface (i.e. the .ui) file.
      custom_widgets -- List of custom widgets (i.e. wdigets not 
                        natively known to QUILoader) to register with
                        the loader.  (e.g. QChartView) 
    """
    if custom_widgets is None: custom_widgets = []

    f = qtc.QFile(ui_fname)
    loader = qtut.QUiLoader()
    for w in custom_widgets:
        loader.registerCustomWidget(w)
    window = loader.load(f)
    f.close()
    return window
    