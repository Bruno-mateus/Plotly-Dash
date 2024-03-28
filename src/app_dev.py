from dash import Dash, html, Input, Output,dcc
from pages.home import home
from pages.page2 import page2
from routes.router import router


## SEÇÃO DE DESENVOLVIMENO

app = Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def initRouter(pathname):
   return router(pathname,[home,page2])

if __name__ == '__main__':
    app.run_server(debug=False, dev_tools_ui=False)  # Ajustado para run_server
