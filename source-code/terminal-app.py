import joblib

model = joblib.load("linear_regression_model.joblib")

def get_input():
    team_exp = float(input("Enter team experience (in years): "))
    manager_exp = float(input("Enter manager experience (in years): "))
    year_end = int(input("Enter year-end (e.g. 85 for 1985): "))
    length = int(input("Enter length of project (in months): "))
    return np.array([team_exp, manager_exp, year_end, length]).reshape(1, -1)

def predict_effort():
    input_data = get_input()
    prediction = model.predict(input_data)
    print(f"The predicted effort required for the project is {prediction[0]:.2f} person-months.")

predict_effort()