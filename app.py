from flask import Flask, render_template, request, redirect, url_for
from threading import Thread
from crawler import crawl
from storage import get_mongo_client
from utils import wait_randomly

app = Flask(__name__)

crawl_status = {
    "is_crawling": False,
    "message": "Idle"
}

def run_crawl(start_url, max_depth):
    global crawl_status
    crawl_status["is_crawling"] = True
    crawl_status["message"] = f"Crawling started for {start_url} with max depth {max_depth}..."
    
    crawl(start_url, max_depth)
    
    crawl_status["is_crawling"] = False
    crawl_status["message"] = "Crawl finished!"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        start_url = request.form["start_url"]
        max_depth = int(request.form["max_depth"])

        crawl_thread = Thread(target=run_crawl, args=(start_url, max_depth))
        crawl_thread.start()

        return redirect(url_for("status"))

    return render_template("index.html")

@app.route("/status")
def status():
    return render_template("status.html", status=crawl_status)

@app.route("/results")
def results():
    db = get_mongo_client()
    collection = db.scraped_data
    scraped_data = list(collection.find())

    return render_template("results.html", data=scraped_data)

if __name__ == "__main__":
    app.run(debug=True)
