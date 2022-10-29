import streamlit as st
import streamlit.components.v1 as components
from src.scrap import scrap
from src.preprocess_text import clean_text
from src.make_wordcloud import make_wordcloud

st.title("BCC BASUDARA")
st.text("Deskripsi blabalbla")
st.markdown("### Cara pemakaian web")
st.text("""
1. Masukkan URL google review tempat wisata yang diinginkan
2. Klik tombol proses
3. Baca hasil visualisasi dan ringkasan untuk evaluasi demi meningkatkan mutu
""")
st.markdown("### Alat blablbalba")
url = st.text_input("Masukkan URL")
jumlah_scroll = st.number_input(
    "Masukkan jumlah scroll", min_value=1, max_value=200, value=5)
button = st.button("proses")
clean_button = st.checkbox("bersihkan data")
hasil_data, hasil_user, hasil_ai, trend_sekitar, summary = st.tabs(
    ["sample data", "hasil user", "hasil analisis sentimen", "trend sekitar jabar", "ringkasan"])

if button:
    with st.spinner("Scrapping data.."):
        data = scrap(url, jumlah_scroll)
    if clean_button:
        with st.spinner("Membersihkan data.."):
            data = clean_text(data)

with hasil_data:
    if not button:
        st.text("masukkan URL terlebih dahulu!")
    else:
        st.table(data.head(10))

with hasil_user:
    if not button:
        st.text("masukkan URL terlebih dahulu!")
    else:
        st.markdown("**Hasil Review Dari User**")
        st.text("Jumlah bintang dari user")
        st.bar_chart(data["bintang"].value_counts())

        bintangs = list(data["bintang"].value_counts().index)
        bintangs.sort(reverse=True)
        for bintang in bintangs:
            texts = " ".join(data[data["bintang"] == bintang]["komentar"])
            if texts.strip() != "":
                st.markdown(f"**Bintang {bintang}**")
                st.pyplot(make_wordcloud(texts))
            else:
                st.markdown(f"**Bintang {bintang}**")
                st.text("Tidak ada komentar")

with hasil_ai:
    if not button:
        st.text("masukkan URL terlebih dahulu!")
    else:
        st.markdown("**Hasil Review Dari User Menggunakan analisis sentimen**")

with trend_sekitar:
    st.markdown("**Trend Pariwisata di Jawa Barat**")
    html = """
<div class='tableauPlaceholder' id='viz1667053767805' style='position: relative'><noscript><a href='#'><img alt='Sheet 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;K4&#47;K4FRB2SP4&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;K4FRB2SP4' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;K4&#47;K4FRB2SP4&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1667053767805');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """
    components.html(html)


with summary:
    if not button:
        st.text("masukkan URL terlebih dahulu!")
    else:
        st.markdown("**Ringkasan**")
        # Komentar2 rating rendah


st.markdown("----")
st.markdown("#### Penjelasan tiap tab")
st.markdown("""
1. tab `sample data` adalah
1. tab `hasil user` adalah
2. tab `hasil analisis sentimen` adalah
3. tab `trend sekitar jabar` adalah
4. tab `ringkasan` adalah
""")

st.markdown("----")
st.markdown("#### FAQ")
st.markdown("""
**Q1**: Bagaimana cara mendapatkan link google review? \\
**A1**:

**Q2**: Kenapa harus ada analisis sentimen, padahal sudah ada rating dari user? \\
**A2**: Karena banyak sekali user yang memberikan rating tidak sesuai dengan komentar 
    yang diberikan. Analisis sentimen akan membantu kita untuk memberi perban
""")
