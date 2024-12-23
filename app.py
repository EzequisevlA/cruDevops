
from flask import  Flask, request, jsonify

app=Flask(__name__)

items=[]
@app.route('/items', methods=['GET'])
def get_items():
	return jsonify(items)

@app.route('/items', methods=['POST'])
def add_items():
	item = request.json
	item.append(item)
	return jsonify(item), 201
@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
	if index >= len(items):
		return jsonify({'error':'Item not found'}), 404
	items[index] = request.json
	return jsonify(items[index])
@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
	if index>= len(items):
		return jsonify({'error': 'Item not found'}), 404
	item = items.pop(index)
	return jsonify(item)
if __name__ == '__main__':
	app.run(debug=True)

