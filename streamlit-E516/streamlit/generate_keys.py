import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Bryant Sundell", "Maciel Lopez", "Ike Honaker", "guest"]
usernames = ["bsundell", "mlopez", "ihonaker", "guest"]
passwords = ["B12qwaszxzxasqw12", "mlopez123", "ihonaker123", "guest123"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pk1"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
