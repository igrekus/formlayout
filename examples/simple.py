# -*- coding: utf-8 -*-
#
# Copyright © 2009 Pierre Raybaut
# Licensed under the terms of the MIT License
# (see formlayout.py for details)

"""
Simple formlayout example

Please take a look at formlayout.py for more examples
(at the end of the script, after the 'if __name__ == "__main__":' line)
"""

from formlayout import fedit

datalist = [('Name', 'Paul'),
            (None, 'Qt.jpg'),
            (None, None),
            (None, 'Information:'),
            ('Password', 'password'),
            ('Age', 30),
            ('Strength', 'slider:10:100:@50'),
            ('Sex', [0, 'Male', 'Female']),
            ('Sex', (0, 'Male', 'Female')),
            ('Size', 12.1),
            ('Eyes', 'green'),
            ('Married', True),
            ('bool list', ['0b110', 'b1', 'b3', 'b4']),
            (None, [('fi&rst', lambda res, wid: print('fun1')), ('s&econd', lambda r, w: print('fun2'))]),
            ('font', ('Arial', 10, False, True)),
            ]

print("result:", fedit(datalist, title="Describe yourself",
                       comment="This is just an <b>example</b>."))
