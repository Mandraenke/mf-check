from flask import Flask, render_template, request, session, redirect, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Decision tree logic
DECISION_TREE = {
    'start': {
        'question': 'Meine Meinungsfreiheit wurde eingeschränkt!',
        'description': 'Lass uns das überprüfen...',
        'next': 'ignored'
    },
    'ignored': {
        'question': 'Wurdest du ignoriert?',
        'ja': {
            'result': 'Deine Meinung wurde nicht eingeschränkt, sie interessiert nur niemanden.',
            'outcome': 'neutral',
            'restart': True
        },
        'nein': 'criticized'
    },
    'criticized': {
        'question': 'Wurdest du kritisiert?',
        'ja': {
            'result': 'Deine Meinung wurde nicht eingeschränkt, sie teilt nur niemand.',
            'outcome': 'neutral',
            'restart': True
        },
        'nein': 'legally_prosecuted'
    },
    'legally_prosecuted': {
        'question': 'Wurdest du juristisch belangt?',
        'nein': {
            'result': 'Du hast deine Meinung geäußert.',
            'outcome': 'success',
            'restart': True
        },
        'ja': 'violated_laws'
    },
    'violated_laws': {
        'question': 'Verstieb deine Aussage gegen geltende Gesetze?',
        'ja': 'read_constitution',
        'nein': {
            'result': 'Du hast Recht.',
            'outcome': 'has_rights'
        }
    },
    'read_constitution': {
        'question': 'Lies die Verfassung.',
        'is_intermediate': True,
        'next': 'final_verdict'
    },
    'final_verdict': {
        'result': 'Du bist ein Depp.',
        'outcome': 'read_constitution'
    }
}


@app.route('/')
def index():
    session.clear()
    session['current_step'] = 'start'
    session['history'] = []
    return render_template('index.html', step=DECISION_TREE['start'])


@app.route('/answer', methods=['POST'])
def answer():
    answer = request.form.get('answer')
    current_step = session.get('current_step', 'start')

    # Store history
    history = session.get('history', [])
    if current_step != 'start':
        current_node = DECISION_TREE[current_step]
        # Don't add intermediate steps to history
        if not current_node.get('is_intermediate', False):
            history.append({
                'question': current_node['question'],
                'answer': answer
            })
    session['history'] = history

    # Navigate the decision tree
    if current_step == 'start':
        next_step = DECISION_TREE[current_step]['next']
        session['current_step'] = next_step
        return render_template('question.html',
                             step=DECISION_TREE[next_step],
                             history=history)

    current_node = DECISION_TREE[current_step]

    # Handle intermediate steps (like "Lies die Verfassung")
    if current_node.get('is_intermediate', False):
        next_step = current_node['next']
        session['current_step'] = next_step
        next_node = DECISION_TREE[next_step]
        if 'result' in next_node:
            return render_template('result.html',
                                 result=next_node,
                                 history=history)
        else:
            return render_template('question.html',
                                 step=next_node,
                                 history=history)

    # Check if we have a result
    if answer.lower() in current_node:
        next_data = current_node[answer.lower()]

        if isinstance(next_data, dict) and 'result' in next_data:
            # We've reached an outcome
            return render_template('result.html',
                                 result=next_data,
                                 history=history)
        else:
            # Continue to next question
            next_step = next_data
            session['current_step'] = next_step
            next_node = DECISION_TREE[next_step]

            # Check if this is an intermediate step
            if next_node.get('is_intermediate', False):
                return render_template('intermediate.html',
                                     step=next_node,
                                     history=history)
            else:
                return render_template('question.html',
                                     step=next_node,
                                     history=history)

    # Fallback
    return redirect(url_for('index'))


@app.route('/restart')
def restart():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
