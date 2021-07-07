import argparse
import json

parser = argparse.ArgumentParser(description='Converts TSV to MySQL\'s INSERT ... ON DUPLICATE KEY UPDATE.')
parser.add_argument('--tsv', metavar='FILE', type=str, help='Path to a TSV file.')
parser.add_argument('--table', metavar='TABLE', type=str, help='Table name.')
parser.add_argument('--column', metavar='INDEX,NAME[,pk][,nullable][,int]', type=str, action='append', help='Column definition.')

args = parser.parse_args()
table = args.table;
columns = [];
encoded_columns = [];

for column_csv in args.column:
    column_info = column_csv.split(',')
    name = column_info[1]
    options = dict.fromkeys(column_info[2:])

    columns.append({
        'index':    int(column_info[0]),
        'name':     name,
        'pk':       'pk' in options,
        'nullable': 'nullable' in options,
        'int':      'int' in options,
    })

    encoded_columns.append('`' + name + '`')

encoded_columns_csv = ','.join(encoded_columns)

with open(args.tsv) as f:
    for line in f:
        values = line.rstrip().split('\t')
        encoded_pairs = []
        encoded_values = []

        for column in columns:
            value = values[column['index']]

            if value != '':
                encoded_value = "'" + value.replace("'", "\\'") + "'"
            elif column['nullable']:
                encoded_value = 'NULL'
            elif column['int']:
                encoded_value = '0'
            else:
                encoded_value = "''"

            encoded_values.append(encoded_value)

            if not column['pk']:
                encoded_pairs.append('`' + column['name'] + '`=' + encoded_value)

        sql = 'INSERT INTO `' + table + '` (' + encoded_columns_csv + ') VALUES (' + ','.join(encoded_values) + ') ON DUPLICATE KEY UPDATE ' + ','.join(encoded_pairs) + ';'

        print(sql)
