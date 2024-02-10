import joblib,pickle

# ['trailingPE', 'priceToBook', 'trailingEps', 'debtToEquity']
new_input = [[8.71,1.96, 35.4, 0]]  # Example input data

''' Loading a better fit model and predicting on a sample input'''
#loaded_model = pickle.load(open('best_stock_LGR.pkl', 'rb'))
loaded_model = joblib.load("best_stock_LGR.pkl")
pred = loaded_model.predict(new_input)
print(round(pred[0],2))

