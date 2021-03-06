import os

import torch
from asciitree import LeftAligned
from flask import Flask, render_template, request

from src.app.forms import SQLForm
from src.data_processor.path_utils import get_model_dir
from src.data_processor.schema_graph import SchemaGraph
from src.demos.demos import Text2SQLWrapper
from src.parse_args import args
from src.trans_checker.args import args as cs_args
from src.utils import utils

os.environ['CUDA_VISIBLE_DEVICES'] = '{}'.format(args.gpu)
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.urandom(32)


def get_answer(db_name, query):
    output = t2sql.process(query, db_name)
    translatable = output['translatable']
    sql_query = output['sql_query']
    confusion_span = output['confuse_span']
    replacement_span = output['replace_span']
    answer = ['Translatable: {}'.format(translatable),
              'Confusion span: {}'.format(confusion_span), 'Replacement span: {}'.format(replacement_span),
              LeftAligned()(schemas[db_name].printable)
              ]
    answer = "\n\n".join(answer)
    return answer, sql_query, translatable


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        database = request.values.get('database')
        query = request.values.get('query')
        answer, sql, translatable = get_answer(database, query)
        schema = schemas[database]
        table_values = dict()
        for key, value in schema.table_rev_index.items():
            result = [tuple(x.name for x in value.fields)]
            result.extend(schema.get_rows(key))
            table_values[value.name] = result
        if translatable:
            execute_result = schema.execute(sql)
        else:
            execute_result = []
    else:
        answer = "An error occurred or you've just loaded a page."
        table_values = {}
        execute_result = []
        sql = "Error!"
    form = SQLForm()
    return render_template('index.html', form=form, answer=answer, table_values=table_values, execute_result = execute_result, sql=sql)


if __name__ == '__main__':
    with torch.no_grad():
        args.model_id = utils.model_index[args.model]
        get_model_dir(args)

        t2sql = Text2SQLWrapper(args, cs_args, None)
        schemas = {}
        for db_name in SQLForm.database.kwargs['choices']:
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
            t2sql.add_schema(schema)
            schemas[db_name] = schema

        app.run(host='0.0.0.0', port=8080)
