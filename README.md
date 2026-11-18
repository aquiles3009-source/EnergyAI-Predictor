EnergyAI Predictor

A machine-learning web application that predicts monthly household electricity consumption based on household characteristics.

Project Overview

EnergyAI Predictor uses a Random Forest regression model to estimate electricity consumption in kilowatt-hours (kWh).

The application allows users to enter:

- Number of occupants
- Average temperature (°C)
- House size (m²)

The model processes these inputs and returns an estimated monthly electricity consumption.

Technologies Used

- Python
- Pandas
- Scikit-learn
- FastAPI
- HTML, CSS and JavaScript
- Git and GitHub
- Render (cloud deployment)

Model Performance

The Random Forest model achieved the following results on the test dataset:

Metric| Result
MAE| 32.01 kWh
RMSE| 41.13 kWh
R²| 0.9419

These metrics describe performance on the project's test dataset and do not establish accuracy for real-world households.

Live Application

"Try EnergyAI Predictor" (https://energyai-predictor.onrender.com)
