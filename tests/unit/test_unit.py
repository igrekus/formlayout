from formlayout import *


def test_qt5_bindings_presence():
    sys.modules.should.have.key('PyQt5.QtGui') or sys.modules.should.have.key('PySide2.QtGui')
    sys.modules.should.have.key('PyQt5.QtCore') or sys.modules.should.have.key('PySide2.QtCore')
    sys.modules.should.have.key('PyQt5.QtWidgets') or sys.modules.should.have.key('PySide2.QtWidgets')


def test_python_veriosn():
    sys.version[0].should.equal('3')


def test_is_text_string():
    is_text_string('string').should.equal(True)
    is_text_string(1).should.equal(False)


def test_is_binary_string():
    is_binary_string(b'string').should.equal(True)
    is_binary_string('string').should.equal(False)


def test_is_string():
    is_string('string').should.equal(True)
    is_string(b'string').should.equal(True)
    is_string(123456).should.equal(False)
    is_string(object()).should.equal(False)


def test_to_text_string():
    to_text_string('string', encoding=None).should.equal('string')
    to_text_string('string', encoding='invalid-encoding').should.equal('string')
    to_text_string('string', encoding='utf-8').should.equal('string')
    to_text_string(b'string', encoding='utf-8').should.equal('string')


def test_colorbutton():
    app = QApplication(sys.argv)
    cb = ColorButton()
    sz = QSize(20, 20)
    ico_sz = QSize(12, 12)
    col = QColor('#ffffffff')
    cb.color = col

    cb.maximumSize().should.equal(sz)
    cb.minimumSize().should.equal(sz)
    cb.iconSize().should.equal(ico_sz)
    cb.color.should.equal(col)

    app.quit()


def test_text_to_qcolor():
    defcol = QColor()
    text_to_qcolor(object()).should.equal(defcol)
    text_to_qcolor(bytes([0x01, 0x02, 0x03])).should.equal(defcol)
    text_to_qcolor('#fffffk').should.equal(defcol)
    text_to_qcolor('asdfghj').should.equal(defcol)
    text_to_qcolor('#ffffffff').should.equal(defcol)
    text_to_qcolor('white').should.equal(QColor('white'))
    text_to_qcolor('#ffffff').should.equal(QColor('#ffffff'))


def test_colorlayout():
    app = QApplication(sys.argv)

    cl = ColorLayout(QColor())
    cl.count().should.equal(2)

    cl.update_color('#ff0000')
    cl.colorbtn.color.should.equal(QColor('#ff0000'))
    cl.lineedit.text().should.equal('#ff0000')
    cl.text().should.equal('#ff0000')

    cl.setStyleSheet('background: black;')
    cl.lineedit.styleSheet().should.equal('background: black;')
    cl.colorbtn.styleSheet().should.equal('background: black;')

    app.quit()


def test_filelayout():
    app = QApplication(sys.argv)

    fl = FileLayout('file: Image: *.jpg')
    fl.dialog_type.should.equal('file: Image: *.jpg')
    fl.count().should.equal(2)

    fl.text().should.equal('')

    fl.setStyleSheet('background: black;')
    fl.lineedit.styleSheet().should.equal('background: black;')

    app.quit()


def test_sliderlayout():
    app = QApplication(sys.argv)

    sl = SliderLayout('slider:10:100:@50')
    sl.slider.tickPosition().should.equal(2)
    sl.slider.minimum().should.equal(10)
    sl.slider.maximum().should.equal(100)
    sl.value().should.equal(50)
    sl.value_label.text().should.equal('50')

    sl.setStyleSheet('background: black;')
    sl.value_label.styleSheet().should.equal('background: black;')
    sl.slider.styleSheet().should.equal('background: black;')

    app.quit()


def test_radiolayout():
    app = QApplication(sys.argv)

    rl = RadioLayout(('rb1', 'rb2'), -1)
    len(rl.group.buttons()).should.equal(2)
    rl.currentIndex().should.equal(-1)

    rl.setStyleSheet('background: black;')
    rl.group.buttons()[0].styleSheet().should.equal('background: black;')

    app.quit()


def test_checklayout():
    app = QApplication(sys.argv)

    cl = CheckLayout(['cb1', 'cb2', 'cb3'], '010')
    len(cl.group.buttons()).should.equal(3)
    cl.values().should.equal([False, True, False])

    cl.setStyleSheet('background: black;')
    cl.group.buttons()[0].styleSheet().should.equal('background: black;')

    app.quit()


def test_pushlayout():
    class ParentMock:
        result = ['stub', 'stub', 'stub']
        def get_dialog(self):
            return None

    app = QApplication(sys.argv)
    pl = PushLayout([
        ['btn1', lambda res, wid: print('btn1')],
        ['btn2', lambda res, wid: print('btn2')]
    ], ParentMock())
    pl.count().should.equal(2)

    app.quit()


def test_countlayout():
    app = QApplication(sys.argv)

    cl = CountLayout(QLineEdit('test'))
    cl.count().should.equal(2)
    cl.text().should.equal('test')
    cl.currentIndex.when.called_with().should.throw(AttributeError)
    cl.n().should.equal(0)

    cl.setStyleSheet('background: black;')
    cl.field.styleSheet().should.equal('background: black;')
    cl.spinbox.styleSheet().should.equal('background: black;')

    app.quit()


def test_font_is_installed():
    app = QApplication(sys.argv)

    font_is_installed('Arial').should.equal(['Arial'])

    app.quit()


def test_tuple_to_qfont():
    app = QApplication(sys.argv)

    tuple_to_qfont(object).should.equal(None)

    font = tuple_to_qfont(('Arial', 10, False, False))
    font.family().should.equal('Arial')
    font.pointSize().should.equal(10)
    font.italic().should.equal(False)
    font.bold().should.equal(False)

    app.quit()


def test_qfont_to_tuple():
    app = QApplication(sys.argv)

    font = QFont()
    font.setFamily('Arial')
    font.setPointSize(10)
    font.setItalic(False)
    font.setBold(False)

    qfont_to_tuple(font).should.equal(('Arial', 10, False, False))

    app.quit()


def test_fontlayout():
    app = QApplication(sys.argv)

    ftup = ('Arial', 2, False, False)
    fl = FontLayout(ftup)

    fl.family.currentFont().family().should.equal('Arial')
    fl.size.model().rowCount().should.equal(19)
    fl.count().should.equal(4)
    fl.italic.isChecked().should.equal(False)
    fl.bold.isChecked().should.equal(False)
    fl.get_font().should.equal(ftup)

    fl.setStyleSheet('background: black;')
    fl.family.styleSheet().should.equal('background: black;')
    fl.size.styleSheet().should.equal('background: black;')
    fl.italic.styleSheet().should.equal('background: black;')
    fl.bold.styleSheet().should.equal('background: black;')

    app.quit()


def test_is_float_valid():
    app = QApplication(sys.argv)

    float_validator = QDoubleValidator()

    str_edit = QLineEdit('test')
    str_edit.setValidator(float_validator)
    is_float_valid(str_edit).should.equal(False)

    float_edit = QLineEdit('1,1')
    float_edit.setValidator(float_validator)
    is_float_valid(float_edit).should.equal(True)

    app.quit()





