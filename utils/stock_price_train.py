import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

raw_data = pd.read_csv("./csvs/train_bse_quality.csv")
# print(raw_data.columns)
x= raw_data[['trailingPE', 'priceToBook', 'trailingEps', 'debtToEquity']]
y = raw_data['currentPrice']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

model = LinearRegression()
model.fit(x_train,y_train)

predictions = model.predict(x_test)

# To Check Predictions
# idx = list(y_test.index)
# for i in range(len(y_test.tolist())):
#     if round(predictions[i],2)>y_test.tolist()[i]:
#         index = idx[i]
#         print(raw_data.iloc[index,6],"-----",y_test.tolist()[i],"-----",round(predictions[i],2))


''' To Predict using trained model (Here results varies after every training)'''

# pred = model.predict([[29.6, 4.06, 18, 0.09]])
# print(round(pred[0],2))

# joblib.dump(model, "stock_LGR.pkl") # To save model

""" Extra functions that can be accessed based on necessity"""

# print(model.coef_)
# print(model.intercept_)
# print(metrics.mean_absolute_error(y_test,predictions))
# print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))

