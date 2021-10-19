
import calendar
import matplotlib.pyplot as plt
from data_processor import DataProcessor

class Visualization:
    def __init__(self):
        self.data=DataProcessor.read_csv("processeddata.csv")
        pass
    def accept_data(self):
        self.train_data =DataProcessor.read_csv("processeddata.csv")
        print(self.train_data.head())
        return self.train_data

    def data_agg(df):
        # select all stores that were open
        store_a= df[df['StoreType']=="b"]
        subs = store_a[store_a['Open']!=0 ]

        # groupby Year and Month
        selected_sales = subs.groupby(['Year', 'Month'])['Sales'].median()
        selected_cust = subs.groupby(['Year', 'Month'])['Customers'].median()
        return selected_sales, selected_cust

    def chart_plot (self, df):
        # plot
        #data = Visualizaton.accept_data() 
        #agg_sales = Visualization.data_agg(self.data)
        store_a= df[df['StoreType']=="b"]
        subs = store_a[store_a['Open']!=0 ]

        # groupby Year and Month
        selected_sales = subs.groupby(['Year', 'Month'])['Sales'].median()
        
        fig, (axis1) = plt.subplots(1,1, figsize=(10,7))
        selected_sales.unstack().T.plot(ax=axis1)
        tmp = axis1.set_title("Store B sales in a year each month")
        tmp = axis1.set_ylabel("Sales")
        tmp = axis1.set_xticks(range(0,13))
        tmp = axis1.set_xticklabels(calendar.month_abbr) 
    
    def group_agg_chart(self, df):
        # group sales/customer data by weekday
        day = df[(df['Open']!=0)]
        sales_day = day.groupby('DayOfWeek')['Sales'].median()
        cust_day = day.groupby('DayOfWeek')['Customers'].median()
        #
        fig, (axis1) = plt.subplots(1,1, sharex=True, figsize=(10,5))
        # plot median sales
        ax1 = sales_day.plot(legend=True, ax=axis1, marker='o',title="Median")
        ax1.set_xticks(sales_day.index)
        tmp = ax1.set_xticklabels(sales_day.index.tolist(), rotation=90)
        # overlay customer data
        cust_day.plot(legend=True, ax=axis1, marker='x', secondary_y=True) 


if __name__ == "__main__":
    obj_viz = Visualization()
    #obj_viz.accept_data()
    obj_viz.chart_plot()