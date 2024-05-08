from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from pycode import Ui_MainWindow

from transformers import pipeline

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.pipe = pipeline("text-generation", model="Daoguang/PyCodeGPT")
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.close_btn.clicked.connect(self.close_window)
        self.maximize_btn.clicked.connect(self.maximize_window)
        self.generate.clicked.connect(self.generate_code)
        self.show()

    def close_window(self):
        self.close()
    
    def maximize_window(self,checked):
        if checked :
            self.showMaximized()
        else:
            self.showNormal()

    def generate_code(self):
        prompt = self.text.toPlainText()

        generated_code = str(self.pipe(prompt,max_length=100,
                            temperature=1.0,
                             top_k=50,
                             top_p=0.95,
                             repetition_penalty=1.0,
                             do_sample=True,
                             num_return_sequences=1
                             )[0]['generated_text'])
        

        k = generated_code.splitlines()

        new = ""

        for i in range(len(k)):
            new = new + str(highlight(k[i], PythonLexer(), HtmlFormatter())) 

        

        html = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
                <html>
                <head><meta name="qrichtext" content="1" /><meta charset="utf-8" />
                    <style>
                    pre { font-family: "Poppins";
                          font-size: 18px;
                          line-height: 100%; }
                    td.linenos .normal { color: #6e7681; background-color: #0d1117; padding-left: 5px; padding-right: 5px; }
                    span.linenos { color: #6e7681; background-color: #0d1117; padding-left: 5px; padding-right: 5px; }
                    td.linenos .special { color: #e6edf3; background-color: #6e7681; padding-left: 5px; padding-right: 5px; }
                    span.linenos.special { color: #e6edf3; background-color: #6e7681; padding-left: 5px; padding-right: 5px; }
                    .highlight .hll { background-color: #6e7681 }
                    .highlight { background: #0d1117; color: #e6edf3 }
                    .highlight .c { color: #8b949e; font-style: italic } /* Comment */
                    .highlight .err { color: #f85149 } /* Error */
                    .highlight .esc { color: #e6edf3 } /* Escape */
                    .highlight .g { color: #e6edf3 } /* Generic */
                    .highlight .k { color: #ff7b72 } /* Keyword */
                    .highlight .l { color: #a5d6ff } /* Literal */
                    .highlight .n { color: #e6edf3 } /* Name */
                    .highlight .o { color: #ff7b72; font-weight: bold } /* Operator */
                    .highlight .x { color: #e6edf3 } /* Other */
                    .highlight .p { color: #e6edf3 } /* Punctuation */
                    .highlight .ch { color: #8b949e; font-style: italic } /* Comment.Hashbang */
                    .highlight .cm { color: #8b949e; font-style: italic } /* Comment.Multiline */
                    .highlight .cp { color: #8b949e; font-weight: bold; font-style: italic } /* Comment.Preproc */
                    .highlight .cpf { color: #8b949e; font-style: italic } /* Comment.PreprocFile */
                    .highlight .c1 { color: #8b949e; font-style: italic } /* Comment.Single */
                    .highlight .cs { color: #8b949e; font-weight: bold; font-style: italic } /* Comment.Special */
                    .highlight .gd { color: #ffa198; background-color: #490202 } /* Generic.Deleted */
                    .highlight .ge { color: #e6edf3; font-style: italic } /* Generic.Emph */
                    .highlight .ges { color: #e6edf3; font-weight: bold; font-style: italic } /* Generic.EmphStrong */
                    .highlight .gr { color: #ffa198 } /* Generic.Error */
                    .highlight .gh { color: #79c0ff; font-weight: bold } /* Generic.Heading */
                    .highlight .gi { color: #56d364; background-color: #0f5323 } /* Generic.Inserted */
                    .highlight .go { color: #8b949e } /* Generic.Output */
                    .highlight .gp { color: #8b949e } /* Generic.Prompt */
                    .highlight .gs { color: #e6edf3; font-weight: bold } /* Generic.Strong */
                    .highlight .gu { color: #79c0ff } /* Generic.Subheading */
                    .highlight .gt { color: #ff7b72 } /* Generic.Traceback */
                    .highlight .g-Underline { color: #e6edf3; text-decoration: underline } /* Generic.Underline */
                    .highlight .kc { color: #79c0ff } /* Keyword.Constant */
                    .highlight .kd { color: #ff7b72 } /* Keyword.Declaration */
                    .highlight .kn { color: #ff7b72 } /* Keyword.Namespace */
                    .highlight .kp { color: #79c0ff } /* Keyword.Pseudo */
                    .highlight .kr { color: #ff7b72 } /* Keyword.Reserved */
                    .highlight .kt { color: #ff7b72 } /* Keyword.Type */
                    .highlight .ld { color: #79c0ff } /* Literal.Date */
                    .highlight .m { color: #a5d6ff } /* Literal.Number */
                    .highlight .s { color: #a5d6ff } /* Literal.String */
                    .highlight .na { color: #e6edf3 } /* Name.Attribute */
                    .highlight .nb { color: #e6edf3 } /* Name.Builtin */
                    .highlight .nc { color: #f0883e; font-weight: bold } /* Name.Class */
                    .highlight .no { color: #79c0ff; font-weight: bold } /* Name.Constant */
                    .highlight .nd { color: #d2a8ff; font-weight: bold } /* Name.Decorator */
                    .highlight .ni { color: #ffa657 } /* Name.Entity */
                    .highlight .ne { color: #f0883e; font-weight: bold } /* Name.Exception */
                    .highlight .nf { color: #d2a8ff; font-weight: bold } /* Name.Function */
                    .highlight .nl { color: #79c0ff; font-weight: bold } /* Name.Label */
                    .highlight .nn { color: #ff7b72 } /* Name.Namespace */
                    .highlight .nx { color: #e6edf3 } /* Name.Other */
                    .highlight .py { color: #79c0ff } /* Name.Property */
                    .highlight .nt { color: #7ee787 } /* Name.Tag */
                    .highlight .nv { color: #79c0ff } /* Name.Variable */
                    .highlight .ow { color: #ff7b72; font-weight: bold } /* Operator.Word */
                    .highlight .pm { color: #e6edf3 } /* Punctuation.Marker */
                    .highlight .w { color: #6e7681 } /* Text.Whitespace */
                    .highlight .mb { color: #a5d6ff } /* Literal.Number.Bin */
                    .highlight .mf { color: #a5d6ff } /* Literal.Number.Float */
                    .highlight .mh { color: #a5d6ff } /* Literal.Number.Hex */
                    .highlight .mi { color: #a5d6ff } /* Literal.Number.Integer */
                    .highlight .mo { color: #a5d6ff } /* Literal.Number.Oct */
                    .highlight .sa { color: #79c0ff } /* Literal.String.Affix */
                    .highlight .sb { color: #a5d6ff } /* Literal.String.Backtick */
                    .highlight .sc { color: #a5d6ff } /* Literal.String.Char */
                    .highlight .dl { color: #79c0ff } /* Literal.String.Delimiter */
                    .highlight .sd { color: #a5d6ff } /* Literal.String.Doc */
                    .highlight .s2 { color: #a5d6ff } /* Literal.String.Double */
                    .highlight .se { color: #79c0ff } /* Literal.String.Escape */
                    .highlight .sh { color: #79c0ff } /* Literal.String.Heredoc */
                    .highlight .si { color: #a5d6ff } /* Literal.String.Interpol */
                    .highlight .sx { color: #a5d6ff } /* Literal.String.Other */
                    .highlight .sr { color: #79c0ff } /* Literal.String.Regex */
                    .highlight .s1 { color: #a5d6ff } /* Literal.String.Single */
                    .highlight .ss { color: #a5d6ff } /* Literal.String.Symbol */
                    .highlight .bp { color: #e6edf3 } /* Name.Builtin.Pseudo */
                    .highlight .fm { color: #d2a8ff; font-weight: bold } /* Name.Function.Magic */
                    .highlight .vc { color: #79c0ff } /* Name.Variable.Class */
                    .highlight .vg { color: #79c0ff } /* Name.Variable.Global */
                    .highlight .vi { color: #79c0ff } /* Name.Variable.Instance */
                    .highlight .vm { color: #79c0ff } /* Name.Variable.Magic */
                    .highlight .il { color: #a5d6ff } /* Literal.Number.Integer.Long */
                    </style>
                </head> 
                <body>'''+new+'''
                </body>
                </html>
            '''
        self.generate.setChecked(False)
        self.result.insertHtml(html) 

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()


    def mouseMoveEvent(self, event):
      self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
      self.dragPos = event.globalPosition().toPoint()
      event.accept()