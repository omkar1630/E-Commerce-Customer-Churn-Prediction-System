from flask import Flask, request, render_template_string
import pandas as pd
import pickle

app = Flask(__name__)

with open("naive_model.pkl", "rb") as file:
    model = pickle.load(file)

gender_map = {
    "Male": 0,
    "Female": 1
}

city_map = {
    "Mumbai": 0,
    "Delhi": 1,
    "Bangalore": 2,
    "Chennai": 3,
    "Hyderabad": 4,
    "Pune": 5,
    "Kolkata": 6
}

subscription_map = {
    "Basic": 0,
    "Standard": 1,
    "Premium": 2
}

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Customer Churn Prediction</title>

<style>

body{
margin:0;
padding:0;
font-family:'Segoe UI',sans-serif;
background:linear-gradient(135deg,#0f172a,#1e293b);
}

.container{
width:700px;
margin:30px auto;
background:white;
padding:30px;
border-radius:20px;
box-shadow:0px 10px 30px rgba(0,0,0,0.3);
}

h1{
text-align:center;
color:#0f172a;
}

.subtitle{
text-align:center;
color:gray;
margin-bottom:20px;
}

.row{
display:flex;
gap:15px;
}

.col{
flex:1;
}

label{
font-weight:bold;
}

input,select{
width:100%;
padding:10px;
margin-top:5px;
margin-bottom:15px;
border-radius:10px;
border:1px solid #ccc;
}

button{
width:100%;
padding:14px;
background:#2563eb;
color:white;
font-size:18px;
border:none;
border-radius:12px;
cursor:pointer;
}

button:hover{
background:#1d4ed8;
}

.result{
margin-top:25px;
padding:20px;
border-radius:15px;
text-align:center;
font-size:22px;
font-weight:bold;
}

.stay{
background:#dcfce7;
color:#15803d;
}

.churn{
background:#fee2e2;
color:#b91c1c;
}

</style>

</head>

<body>

<div class="container">

<h1>📊 Customer Churn Prediction System</h1>

<p class="subtitle">
Predict whether an e-commerce customer is likely to stay or leave.
</p>

<form method="POST">

<div class="row">

<div class="col">
<label>Age</label>
<input type="number" name="age" required>

<label>Gender</label>
<select name="gender">
<option>Male</option>
<option>Female</option>
</select>

<label>City</label>
<select name="city">
<option>Mumbai</option>
<option>Delhi</option>
<option>Bangalore</option>
<option>Chennai</option>
<option>Hyderabad</option>
<option>Pune</option>
<option>Kolkata</option>
</select>

<label>Tenure (Months)</label>
<input type="number" name="tenure" required>

<label>Average Order Value</label>
<input type="number" step="0.01" name="aov" required>

</div>

<div class="col">

<label>Total Orders</label>
<input type="number" name="orders" required>

<label>Last Purchase Days Ago</label>
<input type="number" name="last_purchase" required>

<label>Support Tickets</label>
<input type="number" name="tickets" required>

<label>Subscription Type</label>
<select name="subscription">
<option>Basic</option>
<option>Standard</option>
<option>Premium</option>
</select>

</div>

</div>

<button type="submit">
Predict Customer Status
</button>

</form>

{% if prediction %}

<div class="result {{class_name}}">
{{prediction}}
</div>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():

    prediction = None
    class_name = ""

    if request.method == "POST":

        data = pd.DataFrame([[
            int(request.form["age"]),
            gender_map[request.form["gender"]],
            city_map[request.form["city"]],
            int(request.form["tenure"]),
            float(request.form["aov"]),
            int(request.form["orders"]),
            int(request.form["last_purchase"]),
            int(request.form["tickets"]),
            subscription_map[request.form["subscription"]]
        ]], columns=[
            "age",
            "gender",
            "city",
            "tenure_months",
            "avg_order_value",
            "total_orders",
            "last_purchase_days_ago",
            "support_tickets",
            "subscription_type"
        ])

        result = model.predict(data)[0]

        if result == 1:
            prediction = "⚠️ Customer is likely to Churn"
            class_name = "churn"
        else:
            prediction = "✅ Customer is likely to Stay"
            class_name = "stay"

    return render_template_string(
        HTML,
        prediction=prediction,
        class_name=class_name
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
