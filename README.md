# formlayout

A Python module providing an easy way to create Qt data input form dialogs and widgets.

<img src="https://pythonhosted.org/formlayout/_images/advanced1.png"><img src="https://pythonhosted.org/formlayout/_images/advanced2.png"><img src="https://pythonhosted.org/formlayout/_images/advanced3.png">

Creating forms like these with ``formlayout`` is very easy:
  * Copy ``formlayout.py`` self-sufficient single file script to your project. No dependencies, except for Qt\PyQt, required.
  * Setup the form dialog using a simple ``list`` of parameters (field names, defaults, etc...)
  * Call the ``fedit`` function passing newly created list to show the form dialog.

See [documentation](http://pythonhosted.org/formlayout/) for more details 
(mostly examples) on the library and [changelog](CHANGELOG.md) for recent 
history of changes.

## Overview

Graphical user interface (GUI) libraries are usually designed to address issues which are far more complex than a simple dialog box. As a consequence, creating simple forms and dialogs is generally not as easy as it should be: for simple data input dialogs the feature to SLOC ratio is very low.

``formlayout`` tries to solve this problem by providing the absolute minimum API required to create the form dialog boxes. To show a dialog box, simply call the ``fedit`` function. To setup a dialog box, use lists to pass the required parameters (field names, default values, etc...).

## Simple Example

Here is a simple example (more included in the source package):

```python
from formlayout import fedit
datalist = [('Name', 'Paul'),
            (None, None),
            (None, 'Information:'),
            ('Age', 30),
            ('Sex', [0, 'Male', 'Female']),
            ('Size', 12.1),
            ('Eyes', 'green'),
            ('Married', True),
            ]
fedit(datalist, title="Describe yourself", comment="This is just an <b>example</b>.")
```

<img src="https://pythonhosted.org/formlayout/_images/simple.png">


## Installation

The only requirements are Python, Qt5 and Qt Python bindings:
- Python >=2.6 or Python >=3.2
- Qt >= 5.8 (should work on earlier versions also, but tested only on >= 5.8)
- PyQt5 >= 5.8 or PySide2 >= 5.8

Installation from the source package is straightforward:

```bash
python setup.py install
```
