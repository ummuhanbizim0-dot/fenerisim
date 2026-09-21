
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sinif/<int:sinif_no>')
def sinif(sinif_no):
    return render_template(f'sinif{sinif_no}.html')

@app.route('/oyunlar')
def oyunlar():
    return render_template('oyunlar.html')

@app.route('/quiztest')
def quiztest():
    return render_template('quiztest.html')

@app.route('/deneyler')
def deneyler():
    return render_template('deneyler.html')

@app.route('/blog-haberler')
def blog_haberler():
    return render_template('blog-haberler.html')

@app.route('/hakkinda')
def hakkinda():
    return render_template('hakkinda.html')

@app.route('/iletisim')
def iletisim():
    return render_template('iletisim.html')

@app.route('/tidvideo')
def tidvideo():
    return render_template('tidvideo.html')

@app.route('/pdf-indir')
def pdf_indir():
    return render_template('pdf-indir.html')

@app.route('/sesli-anlatim')
def sesli_anlatim():
    return render_template('sesli-anlatim.html')

@app.route('/sss')
def sss():
    return render_template('sss.html')

@app.route('/konu/<konu_adi>')
def konu(konu_adi):
    return render_template(f'{konu_adi}.html')   

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')