import streamlit as st

st.title("Calculate your sample size")

pop = st.number_input("Target Population Size:", min_value=1, max_value=10000000000, value=10000, step=1)
moe_percent = st.number_input("Margin of Error (%):", min_value=1, max_value=20, value=5, step=1)

ci = st.radio("Confidence Level (%): ", ('90', '95', '99'))

moe = moe_percent/100

if (ci == '90'):
    ss = ((1.65 ** 2) * (0.5 * (1 - 0.5))/(moe ** 2)) / (1 + ((1.65 ** 2) * (0.5 * (1 - 0.5))/((moe ** 2) * pop)))
    st.write(round(ss))

elif (ci == '95'):
    ss = ((1.96 ** 2) * (0.5 * (1 - 0.5))/(moe ** 2)) / (1 + ((1.96 ** 2) * (0.5 * (1 - 0.5))/((moe ** 2) * pop)))
    st.write(round(ss))

else:
    ss = ((2.58 ** 2) * (0.5 * (1 - 0.5))/(moe ** 2)) / (1 + ((2.58 ** 2) * (0.5 * (1 - 0.5))/((moe ** 2) * pop)))
    st.write(round(ss))

