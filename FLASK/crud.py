from flask import *  
import sqlite3  
  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
    return render_template("index.html");  


@app.route("/buscar")
def buscar():
    return render_template("buscar.html")
 
@app.route("/buscarresultado",methods = ["GET", "POST"])
def buscarResultado():
    id = request.form["id"]
    con = sqlite3.connect("employee.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Employees where id="+id)  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  
 

@app.route("/add")  
def add():  
    return render_template("add.html")  
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            address = request.form["address"]  
            with sqlite3.connect("employee.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Employees (name, email, address) values (?,?,?)",(name,email,address))  
                con.commit()  
                msg = "Employee successfully Added"+ name  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            con.close()    
            return render_template("savedetails.html", msg = msg)  
    else:
        return render_template("savedetails.html")
           
 
@app.route("/view")  
def view():  
    con = sqlite3.connect("employee.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Employees")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  
 
 
@app.route("/delete")  
def delete():  
    return render_template("delete.html")  
 
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("employee.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from Employees where id=?",(id,))  
            msg = "record successfully deleted"  
        except:  
            print(sqlite3.Error.mensaje)
            msg = "can't be deleted"
              
        finally:  
            return render_template("deleterecord.html", msg = msg)  
  
if __name__ == "__main__":  
    app.run(debug = True)  