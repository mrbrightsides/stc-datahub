import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="STC DataHub",
    page_icon="📈",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/pwYe3ox.png",
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
    ### 🧩 Apps Showcase
    Lihat disini untuk semua tools yang kami kembangkan:
    [ELPEEF](https://showcase.elpeef.com/)
    
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

import streamlit.components.v1 as components

def embed_iframe(src, hide_top_px=100, hide_bottom_px=0, height=800):
    components.html(f"""
    <style>
        @media (max-width: 768px) {{
            .hide-on-mobile {{
                display: none !important;
            }}
            .show-on-mobile {{
                display: block !important;
                padding: 24px 12px;
                background: #ffecec;
                color: #d10000;
                font-weight: bold;
                text-align: center;
                border-radius: 12px;
                font-size: 1.2em;
                margin-top: 24px;
                animation: fadeIn 0.6s ease-in-out;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            }}
        }}
        @media (min-width: 769px) {{
            .show-on-mobile {{
                display: none !important;
            }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(12px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>

    <!-- Desktop view -->
    <div class="hide-on-mobile" style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:calc(100% + {hide_top_px + hide_bottom_px}px); 
                       border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>

    <!-- Mobile fallback -->
    <div class="show-on-mobile">
        📱 Tampilan ini tidak tersedia di perangkat seluler.<br>
        Silakan buka lewat laptop atau desktop untuk pengalaman penuh 💻
    </div>
    """, height=height + hide_top_px + hide_bottom_px)

# URL Ohara
iframe_url = "https://datahub.elpeef.com/"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=0, hide_bottom_px = -105, height=800)
