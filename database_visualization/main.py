from sqlalchemy import create_engine, MetaData
from flask import Flask
from flask import render_template
app = Flask(__name__)


def get_data_from_db(db_uri):
    engine = create_engine(db_uri)
    metadata = MetaData()
    # reflect db schema to MetaData
    metadata.reflect(bind=engine)
    tables = metadata.tables
    index = 0
    index_mapping = {}
    data = []
    edges = []
    for table_name, table_data in tables.items():
        index_mapping[table_name] = index
        columns_data = []
        for column in table_data.columns:
            if column.foreign_keys:
                foreign_table = [t.column.table.name for t in column.foreign_keys][0]
                if index_mapping.get(table_name) is None:
                    index_mapping[table_name] = len(index_mapping) + 1
                if index_mapping.get(foreign_table) is None:
                    index_mapping[foreign_table] = len(index_mapping) + 1
                edges.append({"from": index_mapping[table_name], "to": index_mapping[foreign_table]})
            columns_data.append(
                f"{column.name} - {str(column.type)}"
            )
        data.append(
            {
                "id": index,
                "label": table_name,
                "columns": "\\n".join(columns_data),
            }
        )
        index += 1
    return data, edges


@app.route('/')
def index():
    db_uri = 'sqlite:///../db.sqlite'
    data, edges = get_data_from_db(db_uri)
    return render_template("template.html", data=data, edges=edges)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")



