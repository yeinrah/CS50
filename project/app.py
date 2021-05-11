from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///library.db")

@app.route("/")
def home():

    sido = db.execute("SELECT DISTINCT 시도명 FROM library ORDER BY 시도명")

    return render_template("index.html", sido = sido)



@app.route("/강원도", methods=["GET", "POST"])
def 강원도():

    강원도 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "강원도")

    if request.method == "POST":

        selectedRegion = request.form.get("강원도")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "강원도")

        return render_template("강원도.html", 강원도=강원도, selectedLibrary=selectedLibrary)

    else:

        return render_template("강원도.html", 강원도=강원도)



@app.route("/경기도", methods=["GET", "POST"])
def 경기도():

    경기도 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "경기도")

    if request.method == "POST":

        selectedRegion = request.form.get("경기도")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "경기도")

        return render_template("경기도.html", 경기도=경기도, selectedLibrary=selectedLibrary)

    else:

        return render_template("경기도.html", 경기도=경기도)



@app.route("/경상남도", methods=["GET", "POST"])
def 경상남도():

    경상남도 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "경상남도")

    if request.method == "POST":

        selectedRegion = request.form.get("경상남도")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "경상남도")

        return render_template("경상남도.html", 경상남도=경상남도, selectedLibrary=selectedLibrary)

    else:

        return render_template("경상남도.html", 경상남도=경상남도)



@app.route("/경상북도", methods=["GET", "POST"])
def 경상북도():

    경상북도 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "경상북도")

    if request.method == "POST":

        selectedRegion = request.form.get("경상북도")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "경상북도")

        return render_template("경상북도.html", 경상북도=경상북도, selectedLibrary=selectedLibrary)

    else:

        return render_template("경상북도.html", 경상북도=경상북도)



@app.route("/광주광역시", methods=["GET", "POST"])
def 광주광역시():

    광주광역시 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "광주광역시")

    if request.method == "POST":

        selectedRegion = request.form.get("광주광역시")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "광주광역시")

        return render_template("광주광역시.html", 광주광역시=광주광역시, selectedLibrary=selectedLibrary)

    else:

        return render_template("광주광역시.html", 광주광역시=광주광역시)



@app.route("/대구광역시", methods=["GET", "POST"])
def 대구광역시():

    대구광역시 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "대구광역시")

    if request.method == "POST":

        selectedRegion = request.form.get("대구광역시")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "대구광역시")

        return render_template("대구광역시.html", 대구광역시=대구광역시, selectedLibrary=selectedLibrary)

    else:

        return render_template("대구광역시.html", 대구광역시=대구광역시)



@app.route("/대전광역시", methods=["GET", "POST"])
def 대전광역시():

    대전광역시 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "대전광역시")

    if request.method == "POST":

        selectedRegion = request.form.get("대전광역시")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "대전광역시")

        return render_template("대전광역시.html", 대전광역시=대전광역시, selectedLibrary=selectedLibrary)

    else:

        return render_template("대전광역시.html", 대전광역시=대전광역시)



@app.route("/부산광역시", methods=["GET", "POST"])
def 부산광역시():

    부산광역시 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "부산광역시")

    if request.method == "POST":

        selectedRegion = request.form.get("부산광역시")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "부산광역시")

        return render_template("부산광역시.html", 부산광역시=부산광역시, selectedLibrary=selectedLibrary)

    else:

        return render_template("부산광역시.html", 부산광역시=부산광역시)



@app.route("/서울특별시", methods=["GET", "POST"])
def 서울특별시():

    서울특별시 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "서울특별시")

    if request.method == "POST":

        selectedRegion = request.form.get("서울특별시")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "서울특별시")

        return render_template("서울특별시.html", 서울특별시=서울특별시, selectedLibrary=selectedLibrary)

    else:

        return render_template("서울특별시.html", 서울특별시=서울특별시)



@app.route("/세종특별자치시", methods=["GET", "POST"])
def 세종특별자치시():

    세종특별자치시 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "세종특별자치시")

    if request.method == "POST":

        selectedRegion = request.form.get("세종특별자치시")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "세종특별자치시")

        return render_template("세종특별자치시.html", 세종특별자치시=세종특별자치시, selectedLibrary=selectedLibrary)

    else:

        return render_template("세종특별자치시.html", 세종특별자치시=세종특별자치시)



@app.route("/울산광역시", methods=["GET", "POST"])
def 울산광역시():

    울산광역시 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "울산광역시")

    if request.method == "POST":

        selectedRegion = request.form.get("울산광역시")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "울산광역시")

        return render_template("울산광역시.html", 울산광역시=울산광역시, selectedLibrary=selectedLibrary)

    else:

        return render_template("울산광역시.html", 울산광역시=울산광역시)



@app.route("/인천광역시", methods=["GET", "POST"])
def 인천광역시():

    인천광역시 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "인천광역시")

    if request.method == "POST":

        selectedRegion = request.form.get("인천광역시")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "인천광역시")

        return render_template("인천광역시.html", 인천광역시=인천광역시, selectedLibrary=selectedLibrary)

    else:

        return render_template("인천광역시.html", 인천광역시=인천광역시)



@app.route("/전라남도", methods=["GET", "POST"])
def 전라남도():

    전라남도 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "전라남도")

    if request.method == "POST":

        selectedRegion = request.form.get("전라남도")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "전라남도")

        return render_template("전라남도.html", 전라남도=전라남도, selectedLibrary=selectedLibrary)

    else:

        return render_template("전라남도.html", 전라남도=전라남도)



@app.route("/전라북도", methods=["GET", "POST"])
def 전라북도():

    전라북도 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "전라북도")

    if request.method == "POST":

        selectedRegion = request.form.get("전라북도")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "전라북도")

        return render_template("전라북도.html", 전라북도=전라북도, selectedLibrary=selectedLibrary)

    else:

        return render_template("전라북도.html", 전라북도=전라북도)



@app.route("/제주특별자치도", methods=["GET", "POST"])
def 제주특별자치도():

    제주특별자치도 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "제주특별자치도")

    if request.method == "POST":

        selectedRegion = request.form.get("제주특별자치도")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "제주특별자치도")

        return render_template("제주특별자치도.html", 제주특별자치도=제주특별자치도, selectedLibrary=selectedLibrary)

    else:

        return render_template("제주특별자치도.html", 제주특별자치도=제주특별자치도)



@app.route("/충청남도", methods=["GET", "POST"])
def 충청남도():

    충청남도 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "충청남도")

    if request.method == "POST":

        selectedRegion = request.form.get("충청남도")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "충청남도")

        return render_template("충청남도.html", 충청남도=충청남도, selectedLibrary=selectedLibrary)

    else:

        return render_template("충청남도.html", 충청남도=충청남도)



@app.route("/충청북도", methods=["GET", "POST"])
def 충청북도():

    충청북도 = db.execute("SELECT DISTINCT 시군구명 FROM library WHERE 시도명 = ? ORDER BY 시군구명", "충청북도")

    if request.method == "POST":

        selectedRegion = request.form.get("충청북도")
        selectedLibrary = db.execute("SELECT 도서관명, 도서관유형, 휴관일, 대출가능권수, 대출가능일수, 소재지도로명주소, 홈페이지주소 FROM library WHERE 시군구명 = ? AND 시도명 = ?", selectedRegion, "충청북도")

        return render_template("충청북도.html", 충청북도=충청북도, selectedLibrary=selectedLibrary)

    else:

        return render_template("충청북도.html", 충청북도=충청북도)

if __name__ == "__main__":
    app.run(debug=True)