import torch
from flask import Flask, render_template, request
import os

from src.data_processor.path_utils import get_model_dir
from src.parse_args import args
from src.app.forms import SQLForm
from src.semantic_parser.learn_framework import EncoderDecoderLFramework

os.environ['CUDA_VISIBLE_DEVICES'] = '{}'.format(args.gpu)
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/', methods=['GET', 'POST'])
def hello():
    database = ""
    query = ""
    if request.method == 'POST':
        database = request.values.get('database')
        query = request.values.get('query')
    form = SQLForm()
    answer = f"{database} {query}"
    return render_template('index.html', form=form, answer=answer)


if __name__ == '__main__':
    with torch.no_grad():
        get_model_dir(args)
        if args.model in ['bridge',
                          'seq2seq',
                          'seq2seq.pg']:
            sp = EncoderDecoderLFramework(args)
        app.run(host='0.0.0.0', port=8080)
