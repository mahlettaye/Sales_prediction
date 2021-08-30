FROM python:3.7
EXPOSE 8501
WORKDIR /Sales_prediction
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD streamlit run app.py
