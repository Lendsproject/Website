from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbandycafe'
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for flash messages

mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        try:
            details = request.form
            print(details)  # Debugging: Print form data
            customerName = details.get('customerName')
            contactNumber = details.get('contactNumber')
            address = details.get('address')
            hotDrinks = details.get('hotDrinks')
            coldDrinks = details.get('coldDrinks')
            orderedMeals = details.get('orderedMeals')
            orderedPasta = details.get('orderedPasta')
            orderedBurger = details.get('orderedBurger')
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO tblorders (customerName, contactNumber, address, hotDrinks, coldDrinks, orderedMeals, orderedPasta, orderedBurger) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                        (customerName, contactNumber, address, hotDrinks, coldDrinks, orderedMeals, orderedPasta, orderedBurger))
            mysql.connection.commit()
            order_id = cur.lastrowid
            cur.close()
            flash('New Order added successfully!')
            return redirect(url_for('view_order', order_id=order_id))
        except Exception as e:
            print(f"Error: {e}")
            flash('An error occurred while processing your order. Please try again.')
            return redirect(url_for('order'))
    return render_template('order.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/view_order/<int:order_id>')
def view_order(order_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tblorders WHERE order_id = %s", (order_id,))
        order = cur.fetchone()
        print(order)  # Debugging: Print fetched order
        cur.close()
        if order:
            return render_template('view_order.html', order=order)
        else:
            flash('Order not found.')
            return redirect(url_for('view_orders'))
    except Exception as e:
        print(f"Error: {e}")
        flash('An error occurred while fetching the order details. Please try again.')
        return redirect(url_for('view_orders'))

@app.route('/view_orders')
def view_orders():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tblorders")
        orders = cur.fetchall()
        print(orders)  # Debugging: Print fetched orders
        cur.close()
        return render_template('view_orders.html', orders=orders)
    except Exception as e:
        print(f"Error: {e}")
        flash('An error occurred while fetching the orders. Please try again.')
        return redirect(url_for('home'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tblorders WHERE order_id = %s", (id,))
        order = cursor.fetchone()
        if request.method == 'POST':
            customerName = request.form['customerName']
            contactNumber = request.form['contactNumber']
            address = request.form['address']
            hotDrinks = request.form['hotDrinks']
            coldDrinks = request.form['coldDrinks']
            orderedMeals = request.form['orderedMeals']
            orderedPasta = request.form['orderedPasta']
            orderedBurger = request.form['orderedBurger']
            cursor.execute("UPDATE tblorders SET customerName = %s, contactNumber = %s, address = %s, hotDrinks = %s, coldDrinks = %s, orderedMeals = %s, orderedPasta = %s, orderedBurger = %s WHERE order_id = %s", 
                           (customerName, contactNumber, address, hotDrinks, coldDrinks, orderedMeals, orderedPasta, orderedBurger, id))
            mysql.connection.commit()
            cursor.close()
            flash('Order updated successfully')
            return redirect(url_for('view_orders'))
        return render_template('edit_order.html', order=order)
    except Exception as e:
        print(f"Error: {e}")
        flash('An error occurred while updating the order. Please try again.')
        return redirect(url_for('view_orders'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM tblorders WHERE order_id = %s", (id,))
        mysql.connection.commit()
        cursor.close()
        flash('Order deleted successfully')
        return redirect(url_for('view_orders'))
    except Exception as e:
        print(f"Error: {e}")
        flash('An error occurred while deleting the order. Please try again.')
        return redirect(url_for('view_orders'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)