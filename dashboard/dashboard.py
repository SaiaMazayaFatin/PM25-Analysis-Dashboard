import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================== KONFIGURASI STREAMLIT ==================
st.set_page_config(
    page_title="Dashboard PM2.5",
    page_icon="🌎",
    layout="wide"
)

# ================== LOAD DATA ==================
file_path = 'dashboard/PRSA_Data_Aotizhongxin_Cleaned.csv'
df = pd.read_csv(file_path)

# Mengubah kolom 'year', 'month', 'day' menjadi datetime
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])

# ================== SIDEBAR NAVIGASI ==================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2917/2917995.png", width=100)
st.sidebar.title("🌎 Dashboard PM2.5")
st.sidebar.markdown("🔎 **Pilih Visualisasi:**")

option = st.sidebar.radio(
    "📊 Pilih Analisis:",
    ["📅 Tren Bulanan PM2.5", "⏳ Distribusi Harian PM2.5", "📊 Kategori Polusi Udara"]
)

# ================== PERTANYAAN 1: Tren Bulanan PM2.5 ==================
if option == "📅 Tren Bulanan PM2.5":
    st.subheader("📈 Tren Bulanan Konsentrasi PM2.5")
    df_monthly = df.groupby(['year', 'month'])['PM2.5'].mean().reset_index()
    df_monthly['year_month'] = df_monthly['year'].astype(str) + '-' + df_monthly['month'].astype(str).str.zfill(2)

    # Plot dengan seaborn
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=df_monthly['year_month'], y=df_monthly['PM2.5'], marker='o', color="blue", linewidth=2)
    plt.xlabel('Bulan-Tahun')
    plt.ylabel('Rata-rata PM2.5 (µg/m³)')
    plt.title('📅 Tren Bulanan PM2.5 (2013-2017)')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig)

# ================== PERTANYAAN 2: Distribusi Harian PM2.5 ==================
elif option == "⏳ Distribusi Harian PM2.5":
    st.subheader("⏳ Distribusi Harian PM2.5 Berdasarkan Jam")
    hourly_avg = df.groupby('hour')['PM2.5'].mean()

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=hourly_avg.index, y=hourly_avg.values, marker='o', color="red", linewidth=2)
    plt.xticks(range(0, 24))
    plt.xlabel("Jam dalam Sehari")
    plt.ylabel("Rata-rata PM2.5 (µg/m³)")
    plt.title("⏳ Distribusi Harian PM2.5")
    plt.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig)

# ================== ANALISIS LANJUTAN: Clustering dengan Binning ==================
elif option == "📊 Kategori Polusi Udara":
    st.subheader("📊 Distribusi Kategori Polusi Udara Berdasarkan PM2.5")

    # Binning PM2.5
    bins = [0, 35, 75, 115, float('inf')]  # Rentang nilai PM2.5
    labels = ['Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi']
    df['Kategori_PM2.5'] = pd.cut(df['PM2.5'], bins=bins, labels=labels, right=False)

    # Hitung jumlah data di setiap kategori
    category_counts = df['Kategori_PM2.5'].value_counts().sort_index()

    # Plot dengan seaborn
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=category_counts.index, y=category_counts.values, palette=['green', 'yellow', 'orange', 'red'])
    plt.xlabel("Kategori PM2.5")
    plt.ylabel("Jumlah Pengamatan")
    plt.title("📊 Distribusi Kategori Polusi Udara")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

# ================== PENUTUP ==================
st.sidebar.markdown("---")
st.sidebar.info("📌 **Catatan:** Data ini dari Stasiun Aotizhongxin (2013-2017).")
st.sidebar.success("📊 **Dashboard oleh Saia Mazaya Fatin**")
