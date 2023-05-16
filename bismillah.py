import streamlit as st
from streamlit_option_menu import option_menu

st.title("Perhitungan Parameter Lingkungan")

with st.sidebar :
    Pilihan = option_menu(menu_title=None,  # required
                        options=['Pendahuluan','Teori','Kalkulator','About Us'],  # required
                        icons=["house", "book", "calculator"],  # optional
                        menu_icon="cast",  # optional
                        default_index=0,  # optional
                        orientation="horizontal",
                        styles={
                            "container": {"padding": "0!important", "background-color": "bbd6b8"},
                            "icon": {"color": "green", "font-size": "25px"},
                            "nav-link": {
                                "font-size": "25px",
                                "text-align": "left",
                                "margin": "0px",
                                "--hover-color": "aec2b6",
                                },
                            "nav-link-selected": {"background-color": "blue"},
                        },
    )


    
#Pendahuluan
if (Pilihan == 'Pendahuluan'):

    st.header(':blue[:earth_africa: SELAMAT DATANG DI WEBAPPS PERHITUNGAN PARAMETER LINGKUNGAN :earth_africa:]')
    st.markdown("""WebApps ini terdiri dari teori dan kalkulator. Teman-teman dapat mengakses teori singkat mengenai TDS, TSS, dan TS yang selanjutnya dapat menghitung nilai TDS, TSS, atau TS pada menu kalkulator.""")
    st.header(':green[:sweat_drops: SELAMAT MENGAKSES! :sweat_drops:]')
    
    

#Teori TDS
elif (Pilihan == 'Teori'):
    
    st.title(":red[:droplet: TOTAL DISSOLVED SOLID :droplet:]")
    
    st.header(":red[:microscope: Prinsip Kerja :microscope:]")
    st.markdown("""Analisis Total Dissolved Solid atau residu terlarut dalam air permukaan dilakukan dengan cara menimbang berat residu sampel yang lolos dari kertas saring berpori 0,45 μm dan telah dikeringkan pada suhu 103-105°C hingga diperoleh bobot tetap.""")
    
    st.header(":red[:desktop_computer: Tujuan Praktikum :desktop_computer:]")
    st.markdown("""Mengetahui kadar Total Dissolved Solid dalam larutan""")
    
    st.header(":red[:hammer_and_wrench: Alat dan Bahan :hammer_and_wrench:]")
    st.markdown("""1. Pinggan penguap yang terbuat dari porselen atau platina atau silica berkualitas tinggi
2. Penangas air
3. Oven untuk pemanasan pada suhu 103-105°C 
4. Desikator
5. Neraca analitik
6. Pipet volumetrik 25 ml
7. Cawan Goch atau alat penyaring lain yang dilengkapi pengisap atau penekan
8. Kertas saring berpori 0,45 μm
9. Tempat khusus untuk menaruh kertas saring
10. Penjepit""")
    
    st.header(":red[:male-office-worker: Cara Kerja :male-office-worker:]")
    st.markdown("""1. Timbang pinggan penguap kosong yang telah dipansakan di oven menggunakan neraca analitik
2. Kocok sampel air permukaan
3. Saring sampel air
4. Pipet 25mL filtrat hasil penyaringan dan masukkan ke dalam pinggan penguap kosong yang telah ditimbang
5. Panaskan dengan penangas air hingga kering, setelah kering lap bagian luar pinggan dengan alkohol
6. Masukkan pinggan penguap ke dalam oven dan panaskan pada suhu 103-105°C selama 1 jam
7. Keluarkan pinggan penguap dan masukkan ke dalam desikator selama 15 menit atau sampai dingin
8. Timbang pinggan penguap yang sudah dingin.""")
    
    st.header(":red[:1234: Perhitungan :1234:]")
    st.latex(r'''
    Bobot TDS \left(\frac{mg}{ml}\right) = 
    \frac{\left(A-B\right) 1000}{volume sampel \left(ml\right)}
    ''')
    st.markdown("""Keterangan: \n
A = Berat cawan berisi residu terlatur dalam (mg) \n
B = Berat cawan kosong (mg) \n
1000 = Konversi dari mL ke L""")
    
    st.header(':red[:droplet: Baku Mutu Standar TDS :droplet:]')
    st.markdown("""Baku mutu standar TDS dapat bervariasi tergantung pada kebutuhan dan regulasi yang berlaku di suatu daerah atau negara. Namun, umumnya baku mutu standar TDS ditetapkan dalam satuan mg/L atau ppm (bagian per juta) dan berkisar antara 500-1000 mg/L untuk air minum dan berkisar antara 1000-3000 mg/L untuk air permukaan dan limbah industri""")

    
    
#Teori TSS

    st.markdown('-----------')
    st.title(":green[:droplet: TOTAL SUSPENDED SOLID :droplet:]")

    st.header(":green[:microscope: Prinsip Kerja :microscope:]")
    st.markdown("""Total Suspended Solid atau padatan tersuspensi total (TSS) adalah residu dari padatan total yang tertahan oleh saringan dengan ukuran partikel maksimal 2μm atau lebih besar dari ukuran partikel koloid. """)

    st.header(":green[:desktop_computer: Tujuan Praktikum :desktop_computer:]")
    st.markdown("Untuk mengetahui total padatan tersuspensi")

    st.header(":green[:hammer_and_wrench: Alat dan Bahan :hammer_and_wrench:]")
    st.markdown("""1. Timbang pinggan penguap kosong yang telah dipanaskan di oven menggunakan neraca analitik
2. Kocok sampel air permukaan
3. Pipet 25 mL sampel air dan masukkan ke dalam pinggan penguap kosong yang telah ditimbang
4. Panaskan dengan penangas air hingga kering, setelah kering lap bagian luar pinggan penguap dengan alkohol
5. Masukkan pinggan penguap ke dalam oven dan panaskan pada suhu 103-105°C selama 1 jam
6. Keluarkan pinggan penguap dan masukkan menit atau sampai dingin ke dalam desikator sela 19/73
7. Timbang pinggan penguap yang sudah dingin.""")

    st.header(":green[:male-office-worker: Cara Kerja :male-office-worker:]")
    st.markdown("""1. Timbang pinggan penguap kosong yang telah dipanaskan di oven menggunakan neraca analitik
2. Kocok sampel air permukaan
3. Pipet 25 ml sampel air dan masukkan ke dalam pinggan penguap kosong yang telah ditimbang
4. Panaskan dengan penangas air hingga kering, setelah kering lap bagian luar pinggan penguap dengan alkohol
5. Masukkan pinggan penguap kedalam oven dan panaskan pada suhu 103-105°C selama 1 jam
6. Keluarkan pinggan penguap dan masukkan menit atau sampai dingin kedalam desikator sela 19/73
7. Timbang pinggan penguap yang sudah dingin.""")

    st.header(":green[:1234: Perhitungan :1234:]")

    st.latex(r'''
    Bobot TSS \left(\frac{mg}{ml}\right) = 
    \frac{\left(A-B\right) 1000}{volume sampel \left(ml\right)}
    ''')

    st.markdown("""Keterangan: \n
A = Berat cawan berisi residu (mg) \n
B = Berat cawan kosong (mg) \n
1000 = Konversi dari mL ke L""")
    
    st.header(':green[:droplet: Baku Mutu Standar TSS :droplet:]')
    st.markdown("""Baku mutu standar TSS dapat berbeda-beda tergantung pada kebutuhan dan regulasi yang berlaku di suatu daerah atau negara. Namun, umumnya baku mutu standar TSS ditetapkan dalam satuan mg/L atau ppm (bagian per juta) dan berkisar antara 30-50 mg/L untuk air permukaan dan 100-300 mg/L untuk limbah domestik dan industri.""")

    
    
#Teori TS
    
    st.markdown('-----------')
    st.title(":blue[:droplet: TOTAL SOLID :droplet:]")

    st.header(":blue[:microscope: Prinsip Kerja :microscope:]")
    st.markdown("""Pengujian Total Solid atau residu total dilakukan dengan cara menimbang berat contoh yang telah dikeringkan pada suhu 103-105°C hingga diperoleh bobot tetap.""")

    st.header(":blue[:desktop_computer: Tujuan Praktikum :desktop_computer:]")
    st.markdown("Mengetahui kadar total solid dalam larutan")

    st.header(":blue[:hammer_and_wrench: Alat dan Bahan :hammer_and_wrench:]")
    st.markdown("""1. Pinggan penguap yang terbuat dari porselen atau tinggi platina atau silica berkualitas
2. Penangas air 
3. Oven untuk pemanasan pada suhu 103-105°C
4. Desikator
5. Neraca analitik
6. Pipet volumetrik 25 mL
7. Penjepit""")

    st.header(":blue[:male-office-worker: Cara Kerja :male-office-worker:]")
    st.markdown("""1. Timbang pinggan penguap kosong yang telah dipanaskan di oven menggunakan neraca analitik
2. Kocok sampel air permukaan
3. Pipet 25 mL sampel air dan masukkan ke dalam pinggan penguap kosong yang telah ditimbang
4. Panaskan dengan penangas air hingga kering, setelah kering lap bagian luar pinggan penguap dengan alkohol
5. Masukkan pinggan penguap ke dalam oven dan panaskan pada suhu 103-105°C selama 1 jam
6. Keluarkan pinggan penguap dan masukkan menit atau sampai dingin kedalam desikator sela 19/73
7. Timbang pinggan penguap yang sudah dingin.""")

    st.header(":blue[:1234: Perhitungan :1234:]")

    st.latex(r'''
    Bobot TS \left(\frac{mg}{ml}\right) = 
    \frac{\left(A-B\right) 1000}{volume sampel \left(ml\right)}
    ''')

    st.markdown("""Keterangan: \n
A = Berat cawan berisi residu (mg) \n
B = Berat cawan kosong (mg) \n
1000 = Konversi dari mL ke L""")
    
    st.header(':blue[:droplet: Baku Mutu Standar TS :droplet:]')
    st.markdown("""Baku mutu standar TS dapat bervariasi tergantung pada kebutuhan dan regulasi yang berlaku di suatu daerah atau negara. Namun, umumnya baku mutu standar TS ditetapkan dalam satuan mg/L atau ppm (bagian per juta) dan berkisar antara 500-1000 mg/L untuk air permukaan dan 2000-4000 mg/L untuk limbah domestik dan industri.""")
    

#Databse
    st.markdown('-----------')
    st.title(":orange[:1234: DATABASE :1234:]")
    from PIL import Image
    image = Image.open('database.jpg')
    st.image(image, caption='database')
    
    
#Kalkulator TDS
elif (Pilihan == 'Kalkulator'):

    st.title(""":red[Kalkulator TDS]""")

    A = st.number_input('Masukkan berat cawan (mg)')
    B = st.number_input('Masukkan nilai berat sampel pada cawan (mg)')
    V = st.number_input('Masukkan volume sampel (mL)')

    tombol = st.button('Hitung nilai TDS')

    if tombol:
        nilai_TDS = (B-A) / V * 1000
        if 500 <= nilai_TDS <= 3000:
            st.success(f'Nilai TDS memenuhi karena {nilai_TDS} masih dalam rentang normal')
        else:
            st.error(f'Nilai TDS tidak memenuhi kebersyaratan baku muku standar karena {nilai_TDS:.2f} di luar rentang normal')
    
    
#Kalkulator TSS
    
    st.markdown('-----------')
    st.title(""":green[Perhitungan TSS]""")

    A = st.number_input('Masukkan nilai berat kertas saring (mg) atau berat cawan + kertas saring')
    B = st.number_input('Masukkan nilai berat sampel pada kertas saring (mg) atau berat cawan sampel + kertas saring residu setelah pemanasan')
    V = st.number_input('Masukkan nilai volume sampel (mL)')

    tombol = st.button('Hitung nilai TSS')

    if tombol:
        nilai_TSS = (B-A) / V * 1000
        if 30 <= nilai_TSS <= 300:
            st.success(f'Nilai TSS memenuhi karena {nilai_TSS} masih dalam rentang normal')
        else:
            st.error(f'Nilai TSS tidak memenuhi kebersyaratan baku muku standar karena {nilai_TSS:.2f} di luar rentang normal')
        
        
#Kalkulator TS
    
    st.markdown('-----------')
    st.title(':blue[Perhitungan TS]')

    A = st.number_input('Masukkan nilai berat cawan akhir + residu(mg)')
    B = st.number_input('Masukkan nilai berat cawan (mg)')
    V = st.number_input('Masukkan nilai volume (mL)')

    tombol = st.button('Hitung nilai TS')

    if tombol:
        nilai_TS = (A-B) / V * 1000
        if 500 <= nilai_TS <= 4000:
            st.success(f'Nilai TS memenuhi karena {nilai_TS} masih dalam rentang normal')
        else:
            st.error(f'Nilai TS tidak memenuhi kebersyaratan baku muku standar karena {nilai_TS:.2f} di luar rentang normal')
        
        
        
#About Us
if (Pilihan == 'About Us'):

    st.title(":orange[About Us]")

    st.markdown("""Assalammualaikum Wr.Wb.
Perkenalkan kami dari mahasiswa/i Politeknik AKA Bogor, memperkenalkan WebApps Perhitungan Parameter Lingkungan yang telah berhasil kami buat. 
Khususnya guna memenuhi nilai mata kuliah Logika Pemrograman Komputer dan kebermanfaatan di industri dalam menghitung parameter lingkungan (TDS, TSS, dan TS).

Tim Penyusun:
1. :cherry_blossom: Aldira Naswa Syahwalia (NIM 2260003)
2. :tulip: Khansa Nur Shafiyah (NIM 2260025)
3. :rose: Nizmi Amalia Samtika (NIM 2260036)
4. :hibiscus: Rivia Sekar Notiyanti (NIM 2260047)
5. :sunflower: Nadya Nafis (NIM 2020356)

Sekian. Semoga WebApps ini bermanfaat bagi teman-teman pengguna.
Wassalammualaikum Wr.Wb.""")
