from flask import Flask , render_template , request , redirect
import youtube_dl

app = Flask(__name__)
@app.route('/')

def index():

    return render_template('index.html')

@app.route('/' , methods=['POST'])
@app.route('/download', methods=["POST", "GET"])
def link():
	url = request.form["url"]
	with youtube_dl.YoutubeDL() as ydl:
		url = ydl.extract_info(url, download=False)
		try:
			download_link = url["entries"][-1]["formats"][-1]["url"]
		except:
			download_link = url["formats"][-1]["url"]
		return redirect(download_link+"&dl=1")

if __name__ == '__main__':
    app.run(port= 8080)