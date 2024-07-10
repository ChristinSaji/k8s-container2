from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_product():
    data = request.get_json()
    file_name = data['file']
    product = data['product']
    
    try:
        total = 0
        with open(f'/christin_PV_dir/{file_name}', 'r') as csvfile:
            lines = csvfile.readlines()
            
            header = [h.strip() for h in lines[0].strip().split(',')]
            if header != ['product', 'amount']:
                raise ValueError("File is not in CSV format")
            
            for line in lines[1:]:
                columns = [col.strip() for col in line.strip().split(',')]
                if len(columns) != 2:
                    raise ValueError("File is not in CSV format")
                
                row_product, row_amount = columns
                if row_product == product:
                    total += int(row_amount)
        
        return jsonify({"file": file_name, "sum": total})
    except Exception as e:
        return jsonify({"file": file_name, "error": "Input file not in CSV format."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)
