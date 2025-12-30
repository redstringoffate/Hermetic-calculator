import streamlit as st
from utils import to_absolute, to_dms
from hermetic_lots import calculate_all_lots
from constants import SIGNS

st.set_page_config(layout="wide")
st.title("🜂 Hermetic Lot Calculator")

sect = st.radio("Sect", ["Day", "Night"], horizontal=True)

DEGREES = list(range(30))
MINUTES = list(range(60))
SECONDS = list(range(60))

st.markdown("---")

positions = {}

for body in ["Asc","Sun","Moon","Mercury","Venus","Mars","Jupiter","Saturn"]:
    st.markdown(f"### {body}")

    # 🔹 헤더 행
    h1, h2, h3, h4 = st.columns([3, 1, 1, 1])
    h1.markdown("**Sign**")
    h2.markdown("**°**")
    h3.markdown("**′**")
    h4.markdown("**″**")

    # 🔹 입력 행
    c1, c2, c3, c4 = st.columns([3, 1, 1, 1])

    with c1:
        sign = st.selectbox(
            "Sign",
            SIGNS,
            key=f"{body}_sign",
            label_visibility="collapsed"
        )
    with c2:
        deg = st.selectbox(
            "Degree",
            DEGREES,
            key=f"{body}_deg",
            label_visibility="collapsed"
        )
    with c3:
        minute = st.selectbox(
            "Minute",
            MINUTES,
            key=f"{body}_min",
            label_visibility="collapsed"
        )
    with c4:
        second = st.selectbox(
            "Second",
            SECONDS,
            key=f"{body}_sec",
            label_visibility="collapsed"
        )

    positions[body] = to_absolute(sign, deg, minute, second)

st.markdown("---")

if st.button("Calculate Hermetic Lots"):
    results = calculate_all_lots(positions, sect)

    st.subheader("Results")
    for name, value in results.items():
        sign, d, m, s = to_dms(value)
        formatted = f"{name}: {sign}, {d}°{m:02d}'{int(round(s)):02d}''"
        st.write(formatted)
