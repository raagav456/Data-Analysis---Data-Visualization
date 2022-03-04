import justpy as jp # justpy is web frame work like flask but in justpy we don't need to write html css and javascript.

def app():
    wp = jp.QuasarPage() # QuarsarPage is a webpage contains many elements that wil added to that page.
                         # It is called quarsar because it uses quarsar framework. It is not related to python it is built with javascript.
    h1 = jp.QDiv(a = wp, text = "Analysis of Course Reviews", classes = "text-h3 text-right q-pa-md")
    # h1 denotess heading QDiv is a quarsar division.
    # fist argument denotes where it belongs
    h2 = jp.QDiv(a = wp, text = "These graphs represent analysis")
    return wp

# wp stands for web page

jp.justpy(app)