# House_Price_Prediction
<h1 align="center">🏠 House Price Prediction – Mini Project</h1>

<p align="center">
Machine Learning Web Application using Custom Linear Regression<br>
Built with Python, Flask & Deployed on Render
</p>

<hr>

<h2>📌 Project Overview</h2>
<p>
This project is a Machine Learning web application that predicts house prices 
based on various features such as location, size, condition, and time of sale.
The model is implemented using Custom Linear Regression (SVD) and deployed online.
</p>

<hr>

<h2>🎯 Objective</h2>
<ul>
<li>Build a predictive model using historical housing data</li>
<li>Develop a user-friendly web interface</li>
<li>Deploy the application online</li>
<li>Provide real-time price predictions</li>
</ul>

<hr>

<h2>📊 Dataset Information</h2>
<ul>
<li><b>Dataset Name:</b> House Sales in King County, USA</li>
<li><b>Source:</b> Kaggle</li>
<li><b>Total Records:</b> 21,613</li>
<li><b>Features:</b> 18 Columns</li>
<li><b>Time Period:</b> May 2014 – May 2015</li>
<li><b>Location:</b> King County, Washington, USA</li>
</ul>

<hr>

<h2>🛠 Technology Stack</h2>

<h3>Backend</h3>
<ul>
<li>Python</li>
<li>Flask</li>
<li>NumPy</li>
<li>Pandas</li>
<li>Scikit-learn (Train-Test Split)</li>
<li>Pickle</li>
</ul>

<h3>Frontend</h3>
<ul>
<li>HTML5</li>
<li>CSS3</li>
</ul>

<h3>Deployment</h3>
<ul>
<li>Render</li>
<li>Gunicorn</li>
</ul>

<hr>

<h2>🗂 Project Structure</h2>

<pre>
House-Price-Prediction/
│
├── app.py
├── model.py
├── MINI_PROJECT.pkl
├── requirements.txt
├── Procfile
├── data.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
</pre>

<hr>

<h2>⚙️ Implementation Steps</h2>

<h3>1️⃣ Environment Setup</h3>
<pre>
python -m venv venv
venv\Scripts\activate
pip install flask numpy pandas scikit-learn gunicorn
</pre>

<h3>2️⃣ Model Development</h3>
<ul>
<li>Custom Linear Regression using SVD</li>
<li>Mean Centering Applied</li>
<li>Calculated Coefficients (m) and Intercept (c)</li>
</ul>

<h3>📈 Evaluation Metrics</h3>
<ul>
<li>RMSE (Root Mean Squared Error)</li>
<li>R² Score</li>
</ul>

<hr>

<h2>🌐 Web Application</h2>

<h3>Routes</h3>
<ul>
<li><b>/</b> → Home Page</li>
<li><b>/predict</b> → Predict House Price</li>
</ul>

<h3>Input Features (17)</h3>
<ul>
<li>Bedrooms</li>
<li>Bathrooms</li>
<li>Sqft Living</li>
<li>Sqft Lot</li>
<li>Floors</li>
<li>Waterfront</li>
<li>View</li>
<li>Condition</li>
<li>Sqft Above</li>
<li>Sqft Basement</li>
<li>Year Built</li>
<li>Year Renovated</li>
<li>City</li>
<li>Country</li>
<li>Year</li>
<li>Month</li>
<li>Day</li>
</ul>

<hr>

<h2>🚀 Deployment (Render)</h2>

<h3>Build Command</h3>
<pre>pip install -r requirements.txt</pre>

<h3>Start Command</h3>
<pre>gunicorn app:app</pre>

<hr>

<h2>📦 Required Files</h2>
<ul>
<li>app.py</li>
<li>requirements.txt</li>
<li>Procfile</li>
<li>MINI_PROJECT.pkl</li>
<li>templates/</li>
<li>static/</li>
</ul>

<hr>

<h2>🔮 Future Enhancements</h2>
<ul>
<li>Random Forest / Gradient Boosting</li>
<li>Hyperparameter tuning</li>
<li>Data visualization dashboard</li>
<li>Export predictions to PDF/Excel</li>
<li>Docker deployment</li>
</ul>

<hr>

<h2>🎓 Conclusion</h2>
<p>
This project demonstrates a complete Machine Learning pipeline from 
data preprocessing to deployment as a live web application.
It showcases full-stack ML development and production deployment skills.
</p>

<hr>

<h2>👨‍💻 Project By</h2>
<p>
<b>B. Vamshi Krishna</b><br>
B.Tech Student<br>
Last Updated: 11-02-2026
</p>
