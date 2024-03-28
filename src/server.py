
from waitress import serve
from app import app  # Substitua 'your_dash_app' pelo nome do módulo da sua aplicação Dash

serve(app.server, host='0.0.0.0', port=8050)