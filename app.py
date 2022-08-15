import cv2
import os
from flask import Flask,render_template,request,url_for,redirect,send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/'
DOWNLOAD_FOLDER = 'static/downloads/'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg','bmp'}

app = Flask(__name__, static_url_path="/static")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 10mb
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method =='POST':
		if 'file' not in request.files:
			print('No file attached in the request')
			return redirect(request.url)
		file=request.files['file']
		if file.filename == '':
			print("no file selected..")
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
			return redirect(url_for('uploaded_file', filename=filename))
	return render_template('index.html')

def process_file(path,filename):
	sketch(path,filename)

def dodgeV2(image, mask):
  return cv2.divide(image, 255-mask, scale=256)

def sketch(path,filename):
	img=cv2.imread(path)
	#cv2.imshow(img)
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_gray_inv = 255 - img_gray
	img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21),
	                            sigmaX=0, sigmaY=0)
	img_blend = dodgeV2(img_gray, img_blur)
	#sketch = 'output_sketch_'+filename
	cv2.imwrite(os.path.join(app.config['DOWNLOAD_FOLDER'] + filename),img_blend)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
	#app.run()
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)