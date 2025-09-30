import streamlit as st
from datetime import datetime, date, timedelta

# 🔯 Zodiac sign finder
def get_zodiac_sign(birthdate):
    day = birthdate.day
    month = birthdate.month
    zodiac = [
        (120, "♑ Capricorn"), (218, "♒ Aquarius"), (320, "♓ Pisces"),
        (420, "♈ Aries"), (521, "♉ Taurus"), (621, "♊ Gemini"),
        (722, "♋ Cancer"), (823, "♌ Leo"), (923, "♍ Virgo"),
        (1023, "♎ Libra"), (1122, "♏ Scorpio"), (1222, "♐ Sagittarius"),
        (1231, "♑ Capricorn")
    ]
    value = month * 100 + day
    for zodiac_date, sign in zodiac:
        if value <= zodiac_date:
            return sign
    return "♑ Capricorn"

# 🧮 Main calculation
def calculate_all(birthdate):
    today = date.today()
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        prev_month = today.month - 1 if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1
        days += (date(today.year, today.month, 1) - date(prev_year, prev_month, 1)).days
    if months < 0:
        years -= 1
        months += 12

    total_days = (today - birthdate).days

    # Next birthday
    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    countdown = next_birthday - today

    weekday = birthdate.strftime('%A')
    zodiac = get_zodiac_sign(birthdate)
    next_milestone = years + 1  # Always next birthday

    return {
        "years": years,
        "months": months,
        "days": days,
        "total_days": total_days,
        "next_birthday": next_birthday,
        "countdown": countdown,
        "weekday": weekday,
        "zodiac": zodiac,
        "next_milestone": next_milestone
    }

# 🌙 Page settings
st.set_page_config(page_title="🎂 Age Calculator", page_icon="🎉", layout="centered")

# 👑 Title
st.title("🎂 Age Calculator with Zodiac, Countdown & Milestones")
st.markdown("Enter your birthdate below to get your full age breakdown:")

# 📅 Date input: year range 2000–2025
min_date = date(2000, 1, 1)
max_date = date(2025, 12, 31)
birthdate = st.date_input("📅 Select your birthdate:", min_value=min_date, max_value=max_date)

# 📌 Calculate button
if st.button("🧮 Calculate Age"):
    if birthdate > date.today():
        st.error("🚫 Birthdate cannot be in the future.")
    else:
        result = calculate_all(birthdate)

        st.success(f"🎉 You are **{result['years']} years, {result['months']} months, {result['days']} days** old.")
        st.info(f"📊 Total days lived: **{result['total_days']:,}** days")
        st.info(f"📅 You were born on a **{result['weekday']}**")
        st.info(f"🔯 Your Zodiac sign: **{result['zodiac']}**")
        st.info(f"🎯 Your next milestone age: **{result['next_milestone']}**")

        st.markdown("---")
        st.markdown(f"🎈 **Next Birthday:** {result['next_birthday'].strftime('%A, %d %B %Y')}")
        st.markdown(f"⏳ Time left: **{result['countdown'].days} days, {result['countdown'].seconds // 3600} hours, {(result['countdown'].seconds % 3600) // 60} mins**")

# 👣 Footer
st.markdown("---")
st.caption("Made with ❤️ by Maheen Touqeer")
