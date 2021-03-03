import torch
from asciitree import LeftAligned
from flask import Flask, render_template, request
import os

from src.data_processor.schema_graph import SchemaGraph
from src.demos.demos import Text2SQLWrapper
from src.utils import utils
from src.data_processor.path_utils import get_model_dir
from src.parse_args import args
from src.trans_checker.args import args as cs_args
from src.app.forms import SQLForm
from src.semantic_parser.learn_framework import EncoderDecoderLFramework

os.environ['CUDA_VISIBLE_DEVICES'] = '{}'.format(args.gpu)
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.urandom(32)


def get_answer(db_name, query):
    db_path = os.path.join(args.db_dir, db_name, '{}.sqlite'.format(db_name))
    schema = SchemaGraph(db_name, db_path=db_path)

    import json
    in_json = os.path.join(args.data_dir, 'tables.json')
    with open(in_json) as f:
        tables = json.load(f)
    for table in tables:
        if table['db_id'] == db_name:
            break
    schema.load_data_from_spider_json(table)

    t2sql = Text2SQLWrapper(args, cs_args, schema)

    output = t2sql.process(query, schema.name)
    translatable = output['translatable']
    sql_query = output['sql_query']
    confusion_span = output['confuse_span']
    replacement_span = output['replace_span']
    answer = [LeftAligned()(schema.printable), 'SQL: {}'.format(sql_query), 'Translatable: {}'.format(translatable),
              'Confusion span: {}'.format(confusion_span), 'Replacement span: {}'.format(replacement_span)]
    answer = "\n".join(answer)
    return answer


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
        args.model_id = utils.model_index[args.model]
        get_model_dir(args)
        # if args.model in ['bridge',
        #                   'seq2seq',
        #                   'seq2seq.pg']:
        #     sp = EncoderDecoderLFramework(args)
        #     sp.cuda()
        app.run(host='0.0.0.0', port=8080)
