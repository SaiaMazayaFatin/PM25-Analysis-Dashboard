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

# ================== SIDEBAR FILTER ==================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2917/2917995.png", width=100)
st.sidebar.title("🌎 Dashboard PM2.5")
st.sidebar.markdown("🔎 **Pilih Visualisasi:**")

option = st.sidebar.radio(
    "📊 Pilih Analisis:",
    ["📜 Tampilkan Data", "📅 Tren Bulanan PM2.5", "⏳ Distribusi Harian PM2.5", "📊 Kategori Polusi Udara"]
)

# FILTERING DATA BERDASARKAN TANGGAL
st.sidebar.markdown("📅 **Filter Tanggal**")
min_date = df['date'].min()
max_date = df['date'].max()
selected_date = st.sidebar.date_input("Pilih Rentang Tanggal:", [min_date, max_date])

# Pastikan data sesuai dengan filter tanggal
if isinstance(selected_date, list) and len(selected_date) == 2:
    df = df[(df['date'] >= pd.to_datetime(selected_date[0])) & (df['date'] <= pd.to_datetime(selected_date[1]))]

# ================== MENAMPILKAN DATA ==================
if option == "📜 Tampilkan Data":
    st.subheader("📜 Tampilkan Data & Statistik")

    # Menampilkan beberapa baris data
    st.write("🔍 **Preview Data:**")
    st.dataframe(df.head(10))

    # Menampilkan statistik deskriptif
    st.write("📊 **Statistik Deskriptif: **")
    st.write(df.describe())

    # Opsi untuk mengunduh dataset
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Unduh Data sebagai CSV", csv, "data_pm25.csv", "text/csv", key='download-csv')

# ================== TREN BULANAN PM2.5 ==================
elif option == "📅 Tren Bulanan PM2.5":
    st.subheader("📈 Tren Bulanan Konsentrasi PM2.5")

    # Checkbox untuk melihat seluruh tahun atau memilih satu tahun
    show_all_years = st.sidebar.checkbox("📊 Tampilkan Seluruh Tahun", value=True)

    if show_all_years:
        df_monthly = df.groupby(['year', 'month'])['PM2.5'].mean().reset_index()
        df_monthly['year_month'] = df_monthly['year'].astype(str) + '-' + df_monthly['month'].astype(str).str.zfill(2)

        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(x=df_monthly['year_month'], y=df_monthly['PM2.5'], marker='o', color="blue", linewidth=2)
        plt.xlabel('Bulan-Tahun')
        plt.ylabel('Rata-rata PM2.5 (µg/m³)')
        plt.title('📅 Tren Bulanan PM2.5 (Semua Tahun)')
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig)

    else:
        selected_year = st.sidebar.selectbox("📅 Pilih Tahun:", df['year'].unique())
        df_filtered = df[df['year'] == selected_year]
        df_monthly = df_filtered.groupby(['month'])['PM2.5'].mean().reset_index()

        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(x=df_monthly['month'], y=df_monthly['PM2.5'], marker='o', color="blue", linewidth=2)
        plt.xlabel('Bulan')
        plt.ylabel('Rata-rata PM2.5 (µg/m³)')
        plt.title(f'📅 Tren Bulanan PM2.5 Tahun {selected_year}')
        plt.xticks(range(1, 13))
        plt.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig)

# ================== DISTRIBUSI HARIAN ==================
elif option == "⏳ Distribusi Harian PM2.5":
    st.subheader("⏳ Distribusi Harian PM2.5 Berdasarkan Jam")

    # Filter jam
    selected_hour = st.sidebar.slider("⏳ Pilih Jam:", 0, 23, (0, 23))
    
    hourly_avg = df[(df['hour'] >= selected_hour[0]) & (df['hour'] <= selected_hour[1])].groupby('hour')['PM2.5'].mean()

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=hourly_avg.index, y=hourly_avg.values, marker='o', color="red", linewidth=2)
    plt.xticks(range(0, 24))
    plt.xlabel("Jam dalam Sehari")
    plt.ylabel("Rata-rata PM2.5 (µg/m³)")
    plt.title(f"⏳ Distribusi Harian PM2.5 ({selected_hour[0]}:00 - {selected_hour[1]}:00)")
    plt.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig)

# ================== KATEGORI POLUSI UDARA ==================
elif option == "📊 Kategori Polusi Udara":
    st.subheader("📊 Distribusi Kategori Polusi Udara Berdasarkan PM2.5")

    bins = [0, 35, 75, 115, float('inf')]
    labels = ['Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi']
    df['Kategori_PM2.5'] = pd.cut(df['PM2.5'], bins=bins, labels=labels, right=False)

    category_counts = df['Kategori_PM2.5'].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=category_counts.index, y=category_counts.values, palette=['green', 'yellow', 'orange', 'red'])
    plt.xlabel("Kategori")
    plt.ylabel("Jumlah Pengamatan")
    plt.title("📊 Distribusi Kategori PM2.5")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

# ================== PENUTUP ==================
st.sidebar.markdown("---")
st.sidebar.success("📊 **Dashboard oleh Saia Mazaya Fatin**")
