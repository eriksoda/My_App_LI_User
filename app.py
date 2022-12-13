
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np



st.markdown("# Are You LinkedIn?")
st.markdown("## Find out below!")

st.markdown("#### Our Data:")
s = pd.read_csv(r"./social_media_usage.csv")


def clean_sm(x):
    x = np.where(x ==1,
                1,
                0)
    return x

ss = pd.DataFrame({
    "income": np.where(s["income"]<= 9, s["income"], np.nan),
    "education": np.where(s["educ2"]<= 8, s["educ2"], np.nan),
    "parent": np.where(s["par"]<= 2, s["par"], np.nan),
    "married": np.where(s["marital"]<= 6, s["marital"], np.nan),
    "female": np.where(s["gender"]<= 2, s["gender"], np.nan),
    "age": np.where(s["age"]<= 97, s["age"], np.nan),
    "Linkedin User": clean_sm(s["web1h"])})

ss.dropna(inplace=True)
st.dataframe(ss)


st.markdown('#### User by Age and Income')
st.markdown('###### Income range represents: 150 or more = 9 to Less than 10k = 1')
sss_chart=alt.Chart(ss).mark_rect().encode(
    alt.X('age', bin=alt.Bin(maxbins=60)),
    alt.Y('income', bin=alt.Bin(maxbins=40)),
    alt.Color('Linkedin User', scale=alt.Scale(scheme='greenblue'))
)
st.altair_chart(sss_chart, use_container_width=True)


st.markdown('#### User by Age and Education')
st.markdown('###### Education range represents: Postgraduate or professional degree = 8 to Less than high school = 1 ')
ss_chart=alt.Chart(ss).mark_circle().encode(
    x='age',
    y='education',
    color='Linkedin User'
)
st.altair_chart(ss_chart, use_container_width=True)

st.markdown("## Make Your Selections!")
###################################################################

Marital = st.selectbox(
    "Marital Status",
    ("Married",
    "Not Married")
)

if Marital == "Married": marital_value = 1
elif Marital == "Not Married": marital_value = 6


###########################################################################
Parent = st.selectbox(
    "Parent",
    ("Yes",
    "No")
)

if Parent == "Yes": parent_value = 1
elif Parent == "No": parent_value = 2

######################################################################################################
gender = st.selectbox(
    "Gender",
    ("Male",
    "Female")
)

if gender == "Male": gender_value = 1
elif gender == "Female": gender_value = 2



############################################################################
Income = st.selectbox(
    "Income",
    ("Upper",
    "Middle",
    "Lower")
)

if Income == "Upper": income_value = 8
elif Income == "Middle": income_value = 6
elif Income == "Lower": income_value = 3



#########################################################################################################

Education = st.selectbox(
    "Education Level",
    ("Postgraduate or professional degree",
    "Some postgraduate",
    "Four-year college",
    "Two-year associate degree",
    "Some college",
    "High school graduate",
    "High school incomplete",
    "Less than high school")
)

if Education == "Postgraduate or professional degree": edu_value = 8
elif Education == "Some postgraduate": edu_value = 7
elif Education == "Four-year college": edu_value = 6
elif Education == "Two-year associate degree": edu_value = 5
elif Education == "Some college": edu_value = 4
elif Education == "High school graduate": edu_value = 3
elif Education == "High school incomplete": edu_value = 2
elif Education == "Less than high school": edu_value = 1

#####################################################################################################



age_value = st.slider("Age",min_value=1,max_value=97)

#################################################################################

lr=LogisticRegression()

y= ss["Linkedin User"]
x= ss[["married","parent","female","income","education","age"]]

x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    stratify=y,
                                                    test_size=0.2,
                                                    random_state=987)


lr.fit(x_train,y_train)                                               

user1 = [marital_value,parent_value, gender_value,income_value, edu_value,age_value]
predict_user = lr.predict([user1])
prob = lr.predict_proba([user1])

if predict_user == 0: predicted_value = "Nope. You're Not LinkedIn"
elif predict_user == 1: predicted_value = "Yup! You're Soooooo LinkedIn"

button_click = st.button("Probs Calculation")

if button_click == True: st.markdown(f"Your Probs is: {prob[0][1]}")
if button_click == True: st.markdown(f"Prediction: {predict_user[0]} - {predicted_value}")

