import dash
from dash import html, dcc, Input, Output, State
import datetime

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Today's To-Do List"),
    
    dcc.Input(id='new-item-input', type='text', placeholder='Enter a new item...'),
    html.Button('Add Item', id='add-button', n_clicks=0),
    
    dcc.Checklist(id='to-do-list'),
    # Hidden div to store the list state
    html.Div(id='list-state', style={'display': 'none'})
])

@app.callback(
    [Output('to-do-list', 'options'),
     Output('to-do-list', 'values'),
     Output('list-state', 'children')],
    [Input('add-button', 'n_clicks')],
    [State('new-item-input', 'value'),
     State('to-do-list', 'values'),
     State('list-state', 'children')],
)
def update_list(n_clicks, new_item, current_values, list_state):
    if n_clicks > 0 and new_item:
        updated_list_state = list_state or []
        updated_list_state.append({'label': f"{datetime.datetime.now():%H:%M} - {new_item}", 'value': new_item})
        
        updated_values = current_values + [new_item]
        
        return updated_list_state, updated_values, updated_list_state

    return list_state or [], current_values, list_state

if __name__ == '__main__':
    app.run_server(debug=True)

