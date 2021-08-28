

import pandas as pd
from joblib import dump,load

from sklearn.model_selection import KFold, cross_val_score,train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
import mlflow
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import accuracy_score,plot_confusion_matrix
import sys
sys.path.insert(0, '/home/mahlet/10ac/Sales_prediction/')

mlflow.set_experiment('dvc_RFR')

class Modeling:


    def __init__(self, filename):
        self.filename = filename
    
    def read_csv (self,filename):
    
        try:
            self.data= pd.read_csv(filename)
        
        except FileNotFoundError as e:
            print ("unable to open")
        
        return self.data

    def data_spliter (df):

        selected_data = df[['Customers','StoreType','CompetitionDistance','Store','Promo','Promo2SinceWeek']]
        X=selected_data
        Y=df['Sales']
        return X, Y

    def train (self):
         #Spliting data into training testing and validation 
         #X_train,X_test,Y_train,Y_test=train_test_split(self.X,self.Y, test_size=0.1, random_state=1)

         #model defination 
         cv = KFold(n_splits=10, random_state=1, shuffle=True)
         #create model
         model = LogisticRegression()
         # evaluate model
         scores = cross_val_score(model, self.df.drop('awarness',axis=1), self.df['awarness'], scoring='accuracy', cv=cv, n_jobs=-1)
         # report performance
         print('Accuracy: %.3f (%.3f)' % (np.mean(scores), np.std(scores)))
   
    def train_mlflow(self,df):
         X,Y= Modeling.data_spliter(df)

         
         mlflow.log_param('input_rows', df.shape[0])
         mlflow.log_param('input_cols', df.shape[1])
         mlflow.log_param('model_type','Logistic Regression')

         X_train,X_test,Y_train,Y_test=train_test_split(X, Y, test_size=0.1, random_state=1)
         model = LogisticRegression()

         model.fit(X_train, Y_train)
         predicted_sales = model.predict(X_test)
         acc = accuracy_score(Y_test, predicted_sales)


         (rmse, mae, r2) = Modeling.eval_metrics(Y_test, predicted_sales)
         mlflow.log_metric("ACC",acc)
         mlflow.log_metric("rmse", rmse)
         mlflow.log_metric("r2", r2)
         mlflow.log_metric("mae", mae)
         # Ploting confusion matrix
         disp = plot_confusion_matrix(model, X_test, Y_test, normalize='true', cmap=plt.cm.Blues)
         plt.savefig('confusion_matrix.png')
         mlflow.log_artifact('confusion_matrix.png')

         with open("logistic regression_metrics.txt", 'w') as outfile:
             outfile.write("rmse: " + str(rmse) + "\n")
             outfile.write("r2: " + str(r2) + "\n")
             outfile.write("mae: " + str(mae) + "\n")
             outfile.write("Accuracy: " + str(acc) + "\n")
        
        
        
    
    

    def train_mlflow_RF(self,df):
         mlflow.set_experiment('DVC_RF')

         X,Y= Modeling.data_spliter(df)

         
         mlflow.log_param('input_rows', df.shape[0])
         mlflow.log_param('input_cols', df.shape[1])
         mlflow.log_param('model_type','Random Forest Regressor')

         X_train,X_test,Y_train,Y_test=train_test_split(X, Y, test_size=0.1, random_state=1)
         model = RandomForestRegressor()

         model.fit(X_train, Y_train)
         predicted_sales = model.predict(X_test)
         #acc = accuracy_score(Y_test, predicted_sales)


         (rmse, mae, r2) = Modeling.eval_metrics(Y_test, predicted_sales)
         #mlflow.log_metric("ACC",acc)
         mlflow.log_metric("rmse", rmse)
         mlflow.log_metric("r2", r2)
         mlflow.log_metric("mae", mae)

         # Ploting confusion matrix
         #disp = plot_confusion_matrix(model, X_test, Y_test, normalize='true', cmap=plt.cm.Blues)
         #plt.savefig('confusion_matrix.png')
         #mlflow.log_artifact('confusion_matrix.png')

         with open("logistic regression_metrics.txt", 'w') as outfile:
             outfile.write("rmse: " + str(rmse) + "\n")
             outfile.write("r2: " + str(r2) + "\n")
             outfile.write("mae: " + str(mae) + "\n")
         
         dump(model,'Xmodel.joblib',3)

         Modeling.plot_feature_importance(model,df)
             

    def plot_feature_importance(model,df):
        # Calculate feature importance in random forest
        importances = model.feature_importances_
        labels = df.columns
        feature_df = pd.DataFrame(list(zip(labels, importances)), columns = ["feature","importance"])
        feature_df = feature_df.sort_values(by='importance', ascending=False,)

        # image formatting
        axis_fs = 18 #fontsize
        title_fs = 22 #fontsize
        sns.set(style="whitegrid")

        ax = sns.barplot(x="importance", y="feature", data=feature_df)
        ax.set_xlabel('Importance',fontsize = axis_fs) 
        ax.set_ylabel('Feature', fontsize = axis_fs)#ylabel
        ax.set_title('Random forest\nfeature importance', fontsize = title_fs)

        plt.tight_layout()
        plt.savefig("feature_importance_v1.png",dpi=120) 
        mlflow.log_artifact("feature_importance.png") 
        
        plt.close()

    
    def eval_metrics(actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
        
        
         




if __name__ =="__main__":
    model_obj= Modeling("data/training.csv")
    data=model_obj.read_csv("data/training.csv")
 
   # model_obj.train_mlflow(data)
    model_obj.train_mlflow_RF(data)
