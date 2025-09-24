import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="STC DataHub",
    page_icon="📈",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/7j5aq4l.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    STC DataHub adalah data hub pariwisata berbasis open-source yang menghubungkan berbagai sumber dataset — dari Kaggle, portal pemerintah, repositori akademik, hingga layanan publik global seperti OpenStreetMap dan InsideAirbnb.

    ---
    #### 🔮 Vision Statement
    > To become the trusted, extensible hub for tourism-related datasets, enabling researchers, developers, and communities to build transparent, verifiable, and innovative solutions for the future of smart tourism.
    
    Dengan STC DataHub, data pariwisata yang tadinya terpecah-pecah, sulit diakses, atau tidak terdokumentasi dengan baik bisa:

    - 📊 Distandardisasi → kolom seragam, format rapi.

    - 🛡️ Dipertanggungjawabkan → setiap dataset punya provenance log.

    - 🌍 Dibagikan lintas ekosistem → siap dipakai untuk riset, dashboard, hingga Web3.
    
    ---
    ### ❓ How to Log in
    
    Untuk menjaga keamanan sekaligus kemudahan akses, STC DataHub mendukung dua mode login:

    1. Local Admin Login (MVP)
    
    - Gunakan akun admin yang sudah terdaftar di .env (ADMIN_EMAIL, ADMIN_PASSWORD).
    
    - Masuk via Admin UI (http://localhost:3000/login)
    
    - Cocok untuk pengujian dan setup awal.
    
    2. Sign-In with Ethereum (SIWE)
    
    - Klik tombol Login with Wallet di UI.
    
    - Hubungkan wallet (MetaMask atau WalletConnect).
    
    - Tandatangani pesan SIWE untuk autentikasi.
    
    - Dataset premium / terbatas bisa diatur hanya bisa diakses oleh wallet yang valid.
    
    ---
    ### 🧩 STC Ecosystem
    1. [STC Analytics](https://stc-analytics.streamlit.app/)
    2. [STC GasVision](https://stc-gasvision.streamlit.app/)
    3. [STC Converter](https://stc-converter.streamlit.app/)
    4. [STC Bench](https://stc-bench.streamlit.app/)
    5. [STC Insight](https://stc-insight.streamlit.app/)
    6. [STC Plugin](https://smartourism.elpeef.com/)
    7. [STC GasX](https://stc-gasx.streamlit.app/)
    8. [STC CarbonPrint](https://stc-carbonprint.streamlit.app/)
    9. [STC ImpactViz](https://stc-impactviz.streamlit.app/)
    10. [DataHub](https://stc-data.streamlit.app/)
    
    ---
    ### ⛓ RANTAI Communities

    🔧 Dev → “Build the chain”
    1. [Numerical Methods Lab](https://metnumlab.streamlit.app/)
    2. [Computational Analytics Studio](https://komnumlab.streamlit.app/)
    3. [BlockPedia](https://blockpedia.streamlit.app/)
    4. [Learn3](https://learn3.streamlit.app/)
    5. [LearnPy](https://rantai-learnpy.streamlit.app/)
    6. [Cruise](https://rantai-cruise.streamlit.app/)
    7. [IndustriX](https://rantai-industrix.streamlit.app/)

    🌐 Net → “Connect the chain”
    1. [SmartFaith](https://smartfaith.streamlit.app/)
    2. [Nexus](https://rantai-nexus.streamlit.app/)
    3. [Decentralized Supply Chain](https://rantai-trace.streamlit.app/)
    4. [ESG Compliance Manager](https://rantai-sentinel.streamlit.app/)
    5. [Decentralized Storage Optimizer](https://rantai-greenstorage.streamlit.app/)
    6. [Cloud Carbon Footprint Tracker](https://rantai-greencloud.streamlit.app/)
    7. [Cloud.Climate.Chain](https://rantai-3c.streamlit.app/)
    8. [Property Management System](https://rantai-pms.streamlit.app/)
    
    🌱 Lab → “Grow the chain”
    1. [BlockBook](https://blockbook.streamlit.app/)
    2. [Data Insights & Visualization Assistant](https://rantai-diva.streamlit.app/)
    3. [Exploratory Data Analysis](https://rantai-exploda.streamlit.app/)
    4. [Business Intelligence](https://rantai-busi.streamlit.app/)
    5. [Predictive Modelling](https://rantai-model-predi.streamlit.app/)
    6. [Ethic & Bias Checker](https://rantai-ethika.streamlit.app/)
    7. [Smart Atlas For Environment](https://rantai-safe.streamlit.app/)
    8. [Blockchain Healthcare Revolution](https://healthchain.streamlit.app/)
    9. [Academic Flow Diagram Generator](https://mermaind.streamlit.app/)
    10. [Decentralized Agriculture](https://agroviz.streamlit.app/)
    
    ---
    #### 🙌 Dukungan & kontributor
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/stc-datahub)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

def embed_iframe(src, hide_top_px=100, hide_bottom_px=0, height=800):
    components.html(f"""
    <div style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:calc(100% + {hide_top_px + hide_bottom_px}px); border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>
    """, height=height + hide_top_px + hide_bottom_px)

# URL Ohara
iframe_url = "https://ohara.ai/mini-apps/miniapp_cmfmsw1y30am90anxbbbb06o2"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=110, hide_bottom_px = 20, height=800)
