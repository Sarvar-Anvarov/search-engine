import utils
import streamlit as st
from search_engine import data
from search_engine.config import settings
from search_engine.main import search_products

# Page config settings
st.set_page_config(
    page_title="PIK Search Engine Demo",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar with options
with st.sidebar:
    st.subheader("PIK Search Engine Demo")
    search_engine = st.selectbox("Выберите модель", options=settings.MODELS_MAPPING.keys())
    top_n = st.number_input("Количество продуктов", min_value=3, max_value=10, step=1)

# Load data
X = data.load_data()

# Search products given request
request = st.text_input("Запрос", "Купить масло для техники")
top_n_ind = search_products(
    request=request, X=X, top_n=top_n,
    search_engine=settings.MODELS_MAPPING[search_engine]()
)


# Display output
df = X.iloc[top_n_ind][["product", "url", "category", "description"]]
df["url"] = df["url"].apply(utils.make_clickable)
df = df.to_html(escape=False)
st.write(df, unsafe_allow_html=True)
