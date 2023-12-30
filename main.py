from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# Define the conversation flow as a dictionary
conversation_flow = {
    'welcome': {
        'options': ['Start', 'Help'],
        'responses': {
            'Start': 'Welcome! Choose an option: Option 1 or Option 2.',
            'Help': 'Sure, I can help you. Please ask me anything.'
        }
    },
    'options': {
        'options': ['Option 1', 'Option 2'],
        'responses': {
            'Option 1': 'You selected Option 1. What do you want to do next?',
            'Option 2': 'You selected Option 2. What do you want to do next?'
        }
    }
    # ... other states can be added similarly
}


@app.route('/', methods=['GET', 'POST'])
def chat():
    current_state = request.form.get('current_state', 'welcome')

    if request.method == 'POST':
        user_input = request.form.get('user_input')

        if user_input in conversation_flow[current_state]['responses']:
            response = conversation_flow[current_state]['responses'].get(user_input, 'Invalid option')
            options = conversation_flow[current_state]['options']
            current_state = 'options'  # Update to the next state
        else:
            response = 'Invalid option'
            options = []

    else:
        # Initial state
        response = conversation_flow[current_state]['responses']['Start']
        options = conversation_flow[current_state]['options']

    return render_template('index.html', options=options, response=response, current_state=current_state)

if __name__ == '__main__':
    app.run(debug=True)
