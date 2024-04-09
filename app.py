import base64
import json
from io import BytesIO

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_caching import Cache

from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)

CORS(app)

cache = Cache(app,config={'CACHE_TYPE': 'simple'})

app = Flask(__name__)

cache.init_app(app)


@app.route('/static/')
@cache.cached(timeout=3600)
def static_file(path):
    app.logger.debug(f"Cache miss for {path}")
    return send_from_directory(app.static_folder, path)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chapter1.html')
def chapter1():
    return render_template('chapter1.html')


@app.route('/chapter2.html')
def chapter2():
    return render_template('chapter2.html')


@app.route('/chapter3.html')
def chapter3():
    return render_template('chapter3.html')


@app.route('/chapter4.html')
def chapter4():
    return render_template('chapter4.html')


@app.route('/chapter5.html')
def chapter5():
    return render_template('chapter5.html')


@app.route('/chapter6.html')
def chapter6():
    return render_template('chapter6.html')


@app.route('/fail1.html')
def fail1():
    return render_template('fail1.html')


@app.route('/fail2.html')
def fail2():
    return render_template('fail2.html')


@app.route('/fail3.html')
def fail3():
    return render_template('fail3.html')


@app.route('/fail3a.html')
def fail3a():
    return render_template('fail3a.html')


@app.route('/fail4a.html')
def fail4a():
    return render_template('fail4a.html')


@app.route('/fail4c.html')
def fail4c():
    return render_template('fail4c.html')


@app.route('/fail5.html')
def fail5():
    return render_template('fail5.html')


@app.route('/fail5b.html')
def fail5b():
    return render_template('fail5b.html')


@app.route('/huizong.html')
def huizong():
    return render_template('huizong.html')


@app.route('/huizong5.html')
def huizong5():
    return render_template('huizong5.html')


@app.route('/jiangyi.html')
def jiangyi():
    return render_template('jiangyi.html')


@app.route('/jiangzhang.html')
def jiangzhang():
    return render_template('jiangzhang.html')


@app.route('/jizhe3.html')
def jizhe3():
    return render_template('jizhe3.html')


@app.route('/jizhe4.html')
def jizhe4():
    return render_template('jizhe4.html')


@app.route('/music2.html')
def music2():
    return render_template('music2.html')


@app.route('/pass1.html')
def pass1():
    return render_template('pass1.html')


@app.route('/pass2.html')
def pass2():
    return render_template('pass2.html')


@app.route('/pass3.html')
def pass3():
    return render_template('pass3.html')


@app.route('/pass4.html')
def pass4():
    return render_template('pass4.html')


@app.route('/pass4b.html')
def pass4b():
    return render_template('pass4b.html')


@app.route('/pass5.html')
def pass5():
    return render_template('pass5.html')


@app.route('/pass5b.html')
def pass5b():
    return render_template('pass5b.html')


@app.route('/6a.html')
def pass6():
    return render_template('6a.html')


@app.route('/6b.html')
def pass6b():
    return render_template('6b.html')


@app.route('/reselect.html')
def reselect():
    return render_template('reselect.html')


@app.route('/start.html')
def start():
    return render_template('start.html')


@app.route('/teach1.html')
def teach1():
    return render_template('teach1.html')


@app.route('/teach2.html')
def teach2():
    return render_template('teach2.html')


@app.route('/teach3a.html')
def teach3a():
    return render_template('teach3a.html')


@app.route('/teach3b.html')
def teach3b():
    return render_template('teach3b.html')


@app.route('/teach4a.html')
def teach4a():
    return render_template('teach4a.html')


@app.route('/teach5.html')
def teach5():
    return render_template('teach5.html')


@app.route('/teach6.html')
def teach6():
    return render_template('teach6.html')

@app.route('/teach6a.html')
def teach6a():
    return render_template('teach6a.html')


@app.route('/test1a.html')
def test1a():
    return render_template('test1a.html')


@app.route('/test1b.html')
def test1b():
    return render_template('test1b.html')


check = [0, 0, 0]


@app.route('/test2.html')
def test2():
    return render_template('test2.html')


@app.route('/test2a.html')
def test2a():
    return render_template('test2a.html')


@app.route('/test2b.html')
def test2b():
    return render_template('test2b.html')


@app.route('/test2c.html')
def test2c():
    return render_template('test2c.html')


@app.route('/test3a.html')
def test3a():
    return render_template('test3a.html')


@app.route('/test3b.html')
def test3b():
    return render_template('test3b.html')


@app.route('/test4a.html')
def test4a():
    return render_template('test4a.html')


@app.route('/test4b.html')
def test4b():
    return render_template('test4b.html')


@app.route('/test5a.html')
def test5a():
    return render_template('test5a.html')


@app.route('/test5b.html')
def test5b():
    return render_template('test5b.html')


@app.route('/test5c.html')
def test5c():
    return render_template('test5c.html')


@app.route('/test5d.html')
def test5d():
    return render_template('test5d.html')


@app.route('/test5e.html')
def test5e():
    return render_template('test5e.html')


@app.route('/test5f.html')
def test5f():
    return render_template('test5f.html')


@app.route('/test6a.html')
def test6a():
    return render_template('test6a.html')


@app.route('/test6c.html')
def test6c():
    return render_template('test6c.html')


@app.route('/v1.html')
def v1():
    return render_template('v1.html')


@app.route('/v2.html')
def v2():
    return render_template('v2.html')


@app.route('/v3.html')
def v3():
    return render_template('v3.html')


@app.route('/v4.html')
def v4():
    return render_template('v4.html')


@app.route('/v5.html')
def v5():
    return render_template('v5.html')


@app.route('/v6.html')
def v6():
    return render_template('v6.html')


@app.route('/video3.html')
def video3():
    return render_template('video3.html')


@app.route('/zhangjiezhanshi.html')
def zhangjiezhanshi():
    return render_template('zhangjiezhanshi.html')


@app.route('/zhishidian.html')
def zhishidian():
    return render_template('zhishidian.html')


@app.route('/dashipin.html')
def dashipin():
    return render_template('dashipin.html')


@app.route('/v0.html')
def v0():
    return render_template('v0.html')


answer = {
}


@app.route('/api/test1a', methods=['POST'])
def receive_data():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    answer["test1a"] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)

    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/test1b', methods=['POST'])
def receive_datatest1b():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    answer["test1b"] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)

    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/test2a', methods=['POST'])
def receive_datatest2a():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    answer["test2a"] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)

    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/test2b', methods=['POST'])
def receive_datatest2b():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    answer["test2b"] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)
    print(answer)
    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/test2c', methods=['POST'])
def receive_datatest2c():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    answer["test2c"] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)
    print(answer)
    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/test3a', methods=['POST'])
def receive_datatest3a():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    answer["test3a"] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)
    print(answer)
    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/test4a', methods=['POST'])
def receive_datatest4a():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    answer["test4a"] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)
    print(answer)
    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/test5d', methods=['POST'])
def receive_datatest5d():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    answer["test5d"] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)
    print(answer)
    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/test5e', methods=['POST'])
def receive_datatest5e():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    answer["test5e"] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)
    print(answer)
    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/test5f', methods=['POST'])
def receive_datatest5f():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    answer["test5f"] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)
    print(answer)
    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


chapter = {}


@app.route('/api/test6c', methods=['POST'])
def receive_datatest6c():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    answer["test6c"] = data
    answer["test5"] = answer["test5d"] + answer["test5e"] + answer["test5f"]
    answer["test2"] = answer["test2a"] + answer["test2b"] + answer["test2c"]

    del answer["test2a"]
    del answer["test2b"]
    del answer["test2c"]
    del answer["test5d"]
    del answer["test5e"]
    del answer["test5f"]
    # 在服务器端打印收到的数据
    print("Received data:", data)
    print(answer)

    merged = {**chapter, **answer}

    merged_str = json.dumps(merged, separators=(',', ':'))
    with open('data.txt', 'a') as file:
        file.write(merged_str + '\n')

    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/chapter1', methods=['POST'])
def receive_chapter1data():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    chapter[1] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)

    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/chapter2', methods=['POST'])
def receive_chapter2data():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    chapter[2] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)

    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/chapter3', methods=['POST'])
def receive_chapter3data():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    chapter[3] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)

    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/chapter4', methods=['POST'])
def receive_chapter4data():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    chapter[4] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)

    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/chapter5', methods=['POST'])
def receive_chapter5data():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    chapter[5] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)

    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


@app.route('/api/chapter6', methods=['POST'])
def receive_chapter6data():
    # 通过 request 对象获取 JSON 数据
    data = request.get_json()
    chapter[6] = data
    # 在服务器端打印收到的数据
    print("Received data:", data)
    print(chapter)
    # 在这里处理数据，然后可以返回响应给客户端
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)


def plot_pie_chart(scores, title, x):
    sizes = list(scores.values())
    labels = [f'{key}分' for key in scores.keys()]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title(title)
    pie_chart_bytesio = BytesIO()
    plt.savefig(x, format='png')
    plt.close()
    return pie_chart_bytesio


matplotlib.use('Agg')

api = Api(app)


class TeacherResource(Resource):
    def get(self):
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体
        plt.rcParams['axes.unicode_minus'] = False
        data = []
        # 假设数据存储在data.txt文件中，每行是一个JSON对象
        with open('data.txt', 'r') as file:
            for line_number, line in enumerate(file, start=1):
                # 忽略空行
                if not line.strip():
                    continue

                try:
                    json_object = json.loads(line)
                    data.append(json_object)
                except json.decoder.JSONDecodeError as e:
                    print(f"Error decoding JSON on line {line_number}: {e}")
                    print(f"Problematic line content: {line}")
                    # 如果遇到错误，可以选择跳过当前行并继续解析下一行
                    continue

        df = pd.DataFrame(data)
        plots_data = generate_plots(df)
        # 将 Base64 编码的图形数据添加到响应体
        response_data = {}
        for plot_name, plot_bytesio in plots_data.items():
            response_data[f'{plot_name}_data'] = base64.b64encode(plot_bytesio.getvalue()).decode('utf-8')

        return response_data


api.add_resource(TeacherResource, '/api/teacher')


@app.route('/teacher', methods=['get'])
def showdata():
    return render_template('teacher.html')


def generate_plots(df):
    # 统计键值为 "1" 中为1的个数
    chap1 = df[df['1'] == 1]['1'].count() / len(df)
    chap2 = df[df['2'] == 1]['2'].count() / len(df)
    chap3 = df[df['3'] == 1]['3'].count() / len(df)
    chap4 = df[df['4'] == 1]['4'].count() / len(df)
    chap5 = df[df['5'] == 1]['5'].count() / len(df)
    chap6 = df[df['6'] == 1]['6'].count() / len(df)



    test1a1 = df[df['test1a'].apply(lambda x: isinstance(x, list) and len(x) > 0 and x[0] == 1)]['test1a'].count() / len(df)
    test1a2 = df[df['test1a'].apply(lambda x: isinstance(x, list) and len(x) > 0 and x[1] == 1)]['test1a'].count() / len(df)
    test1a3 = df[df['test1a'].apply(lambda x: isinstance(x, list) and len(x) > 0 and x[2] == 1)]['test1a'].count() / len(df)

    if 'test1b' in df.columns:
        test1b1 = df[df['test1b'].apply(lambda x: isinstance(x, list) and len(x) > 0 and x[0] == 1)]['test1b'].count() / len(df)
        test1b2 = df[df['test1b'].apply(lambda x: isinstance(x, list) and len(x) > 0 and x[1] == 1)]['test1b'].count() / len(df)
        test1b3 = df[df['test1b'].apply(lambda x: isinstance(x, list) and len(x) > 0 and x[2] == 1)]['test1b'].count() / len(df)
    else:
        test1b1 = 0
        test1b2 = 0
        test1b3 = 0

    test3a = df[df['test3a'] == 1]['test3a'].count() / len(df)
    test4a = df[df['test4a'] == 1]['test4a'].count() / len(df)
    test6c = df[df['test6c'] == 1]['test6c'].count() / len(df)

    test2_list = df['test2'].value_counts(normalize=True).to_dict()
    test5_list = df['test5'].value_counts(normalize=True).to_dict()

    lista = [chap1, chap2, chap3, chap4, chap5, chap6, test1a1, test1a2, test1a3, test1b1, test1b2, test1b3, test3a,
             test4a, test6c]

    score2 = {"test2": test2_list}
    score5 = {"test5": test5_list}

    labels = ['第一章选择', '第二章选择', '第三章选择', '第四章选择', '第五章选择', '第六章选择', '第一章练习题1.1',
              '第一章练习题1.2', '第一章练习题1.3', '第一章练习题2.1',
              '第一章练习题2.2', '第一章练习题2.3', '第三章练习题', '第四章练习题', '第六章连线题']
    values = lista
    histogram_bytesio = BytesIO()
    figure_width = 25
    plt.figure(figsize=(figure_width, len(labels) * 0.5))
    plt.bar(labels, values)
    plt.xlabel('答题统计')
    plt.ylabel('正确率')

    plt.title('各章选择题正确率统计图')
    for label, value in zip(labels, values):
        plt.text(label, value + 0.01, f'{value:.2%}', ha='center')
    plt.savefig(histogram_bytesio, format='png')
    plt.clf()

    # 保存score2的饼图
    pie_chart2_bytesio = BytesIO()
    plot_pie_chart(score2['test2'], '第二章得分', pie_chart2_bytesio)
    plt.clf()

    # 保存score5的饼图
    pie_chart5_bytesio = BytesIO()
    plot_pie_chart(score5['test5'], '第五章得分', pie_chart5_bytesio)

    plt.clf()
    plt.close()
    return {
        'histogram': histogram_bytesio,
        'pie_chart2': pie_chart2_bytesio,
        'pie_chart5': pie_chart5_bytesio
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False, threaded=True)
