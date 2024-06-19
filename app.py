
import streamlit as st
import numpy as np
from predict import load_model, predict_obesity

# Modeli ve scaler'ı yükleyin
model, scaler = load_model()

# Streamlit başlığı
st.title("Obezite Tahmin Arayüzü")

# Kullanıcıdan giriş verilerini alın
gender = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])
age = st.slider("Yaş", 10, 100)
height = st.number_input("Boy (cm)")
weight = st.number_input("Kilo (kg)")
family_history_with_overweight = st.selectbox("Ailede Obezite Öyküsü", ["Evet", "Hayır"])
frequent_consumption_of_high_caloric_food = st.selectbox("Yüksek Kalorili Gıda Tüketimi", ["Evet", "Hayır"])
smoking = st.selectbox("Sigara Kullanımı", ["Evet", "Hayır"])
calories_consumption_monitoring = st.selectbox("Kalori Tüketimi Takibi", ["Evet", "Hayır"])
physical_activity_frequency = st.selectbox("Fiziksel Aktivite Sıklığı", ["Yok", "Haftada 1-2", "Haftada 3-4", "Haftada 5-7"])
time_using_technology_devices = st.selectbox("Teknolojik Cihaz Kullanım Süresi", ["<1 saat", "1-2 saat", "2-3 saat", "3-5 saat", "5-7 saat", ">7 saat"])
consumption_of_water_daily = st.selectbox("Günlük Su Tüketimi", ["<1 litre", "1-2 litre", "2-3 litre", "3-4 litre", ">4 litre"])
consumption_of_alcohol = st.selectbox("Alkol Tüketimi", ["Hiç", "Nadiren", "Haftada 1-2", "Haftada 3-4", "Haftada 5-7", "Her gün"])
transportation_used = st.selectbox("Ulaşım Şekli", ["Özel Araç", "Toplu Taşıma", "Bisiklet", "Yürüyerek"])

# Giriş verilerini bir listeye ekleyin
user_data = np.array([
    1 if gender == "Erkek" else 0,
    age,
    height,
    weight,
    1 if family_history_with_overweight == "Evet" else 0,
    1 if frequent_consumption_of_high_caloric_food == "Evet" else 0,
    1 if smoking == "Evet" else 0,
    1 if calories_consumption_monitoring == "Evet" else 0,
    ["Yok", "Haftada 1-2", "Haftada 3-4", "Haftada 5-7"].index(physical_activity_frequency),
    ["<1 saat", "1-2 saat", "2-3 saat", "3-5 saat", "5-7 saat", ">7 saat"].index(time_using_technology_devices),
    ["<1 litre", "1-2 litre", "2-3 litre", "3-4 litre", ">4 litre"].index(consumption_of_water_daily),
    ["Hiç", "Nadiren", "Haftada 1-2", "Haftada 3-4", "Haftada 5-7", "Her gün"].index(consumption_of_alcohol),
    ["Özel Araç", "Toplu Taşıma", "Bisiklet", "Yürüyerek"].index(transportation_used)
]).reshape(1, -1)

# Tahmini yapın
prediction, prediction_proba = predict_obesity(model, scaler, user_data)

# Tahmini gösterin
st.subheader("Tahmin Sonucu")
st.write("Obezite Durumu:", "Evet" if prediction[0] == 1 else "Hayır")
st.write("Tahmin Olasılığı: {:.2f}%".format(prediction_proba[0][1] * 100))