from dash import  html,dcc

def page2():
    return html.Div([
        html.H1('Hello world page 2'),
        dcc.Link('Return to home',href='/')
    ])