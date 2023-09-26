from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
  { 
    'id': 1,
    'titulo': 'Mitologia Nórdica',
    'autor': 'Thomas'
  },
  
  { 
    'id': 2,
    'titulo': 'A evolução da Física',
    'autor': 'Albert Einstein'
  },
  
  { 
    'id': 3,
    'titulo': 'Código Limpo',
    'autor': 'Martin'
  }
]

# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_id(id):
    for livro in livros:
      if livro.get('id') == id:
        return jsonify(livro)
 
# Editar
# Excluir


app.run(port=5000, host='localhost', debug=True)

