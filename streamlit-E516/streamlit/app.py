import pickle
import streamlit as st
import pandas as pd
import boto3
from io import BytesIO

import streamlit_authenticator as stauth
from pathlib import Path


st.set_page_config(page_title="Animal Classifier!")
st.title("Animal Classifier! - E516 - Spring 2024")



# --- USER AUTHENTICATION ---

names = ["Bryant Sundell", "Maciel Lopez", "Ike Honaker", "guest"]
usernames = ["bsundell", "mlopez", "ihonaker", "guest"]

file_path = Path(__file__).parent / "hashed_pw.pk1"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator =  stauth.Authenticate(names, usernames, hashed_passwords,
    "animal_classifier", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:

    if st.session_state["authentication_status"]:
        try:
            authenticator.logout("Logout", "sidebar") 
        except KeyError:
            pass  # ignore it
        except Exception as err:
            st.error(f'Unexpected exception {err}')
            raise Exception(err)

    st.sidebar.title(f"Welcome {name}")
    st.sidebar.markdown("Upload a file to S3")

    with st.sidebar:
        # upload file to s3 bucket
        uploaded_file = st.file_uploader("Upload a file", type=["png", "jpeg", "tiff"])
        s3_bucket_name = 'animal-classifier516'

        # save uploaded file to s3 bucket
        if uploaded_file is not None:
            s3 = boto3.resource('s3')
            s3.Bucket(s3_bucket_name).put_object(Key=uploaded_file.name, Body=uploaded_file)
            st.write("File uploaded to S3 bucket.")

        # select file from s3 bucket
        s3 = boto3.client('s3')
        response = s3.list_objects_v2(Bucket=s3_bucket_name)

        file_list = []
        # Check if there are any items in the s3 bucket, if there are, add them to the file_list, if there aren't display a message
        if 'Contents' in response:
            for obj in response['Contents']:
                file_list.append(obj['Key'])
        else:
            st.write("No files in S3 bucket")

        selected_file = st.selectbox("Images that have been uploaded", file_list, placeholder="Select a file from S3 bucket", index=None)
        st.sidebar.write("You selected: ", selected_file)


        if selected_file is None:
            st.write("Please select a file from S3 bucket")
        else:
            # download file from s3 bucket
            s3 = boto3.client('s3')
            response = s3.get_object(Bucket=s3_bucket_name, Key=selected_file)
            file_stream = BytesIO(response['Body'].read())

            st.image(file_stream)


    with st._main:
        returned_mammal_s3_bucket_name = 'returned-mammal-photos'

        # select file from s3 bucket
        s3 = boto3.client('s3')
        mammal_response = s3.list_objects_v2(Bucket=returned_mammal_s3_bucket_name)

        mammal_file_list = []
        # Check if there are any items in the s3 bucket, if there are, add them to the file_list, if there aren't display a message
        if 'Contents' in mammal_response:
            for obj in mammal_response['Contents']:
                mammal_file_list.append(obj['Key'])
        else:
            st.write("No files in S3 bucket")

        mammal_file_returned = st.selectbox("View mammal Photos Uploaded", mammal_file_list, placeholder="Select a file from S3 bucket", index=None)
        st.write("You selected: ", mammal_file_returned)


        if mammal_file_returned is None:
            st.write("")
        else:
            # download file from s3 bucket
            s3 = boto3.client('s3')
            mammal_response = s3.get_object(Bucket=returned_mammal_s3_bucket_name, Key=mammal_file_returned)
            mammal_file_stream = BytesIO(mammal_response['Body'].read())

            st.image(mammal_file_stream)

        returned_amphibian_s3_bucket_name = 'returned-amphibian-photos'

        # select file from s3 bucket
        s3 = boto3.client('s3')
        amphibian_response = s3.list_objects_v2(Bucket=returned_amphibian_s3_bucket_name)

        amphibian_file_list = []
        # Check if there are any items in the s3 bucket, if there are, add them to the file_list, if there aren't display a message
        if 'Contents' in amphibian_response:
            for obj in amphibian_response['Contents']:
                amphibian_file_list.append(obj['Key'])
        else:
            st.write("No files in S3 bucket")

        amphibian_file_returned = st.selectbox("View amphibian Photos Uploaded", amphibian_file_list, placeholder="Select a file from S3 bucket", index=None, key='ambibian_select_box')
        st.write("You selected: ", amphibian_file_returned)


        if amphibian_file_returned is None:
            st.write("")
        else:
            # download file from s3 bucket
            s3 = boto3.client('s3')
            amphibian_response = s3.get_object(Bucket=returned_amphibian_s3_bucket_name, Key=amphibian_file_returned)
            amphibian_file_stream = BytesIO(amphibian_response['Body'].read())

            st.image(amphibian_file_stream)

        returned_arthropod_s3_bucket_name = 'returned-arthropod-photos'

        # select file from s3 bucket
        s3 = boto3.client('s3')
        arthropod_response = s3.list_objects_v2(Bucket=returned_arthropod_s3_bucket_name)

        arthropod_file_list = []
        # Check if there are any items in the s3 bucket, if there are, add them to the file_list, if there aren't display a message
        if 'Contents' in arthropod_response:
            for obj in arthropod_response['Contents']:
                arthropod_file_list.append(obj['Key'])
        else:
            st.write("No files in arthropod S3 bucket")

        arthropod_file_returned = st.selectbox("View arthropod Photos Uploaded", arthropod_file_list, placeholder="Select a file from S3 bucket", index=None, key='arthropod_select_box')
        st.write("You selected: ", arthropod_file_returned)


        if arthropod_file_returned is None:
            st.write("")
        else:
            # download file from s3 bucket
            s3 = boto3.client('s3')
            arthropod_response = s3.get_object(Bucket=returned_arthropod_s3_bucket_name, Key=arthropod_file_returned)
            arthropod_file_stream = BytesIO(arthropod_response['Body'].read())

            st.image(arthropod_file_stream)

        returned_bird_s3_bucket_name = 'returned-bird-photos'

        # select file from s3 bucket
        s3 = boto3.client('s3')
        bird_response = s3.list_objects_v2(Bucket=returned_bird_s3_bucket_name)

        bird_file_list = []
        # Check if there are any items in the s3 bucket, if there are, add them to the file_list, if there aren't display a message
        if 'Contents' in bird_response:
            for obj in bird_response['Contents']:
                bird_file_list.append(obj['Key'])
        else:
            st.write("No files in bird S3 bucket")

        bird_file_returned = st.selectbox("View bird Photos Uploaded", bird_file_list, placeholder="Select a file from S3 bucket", index=None, key='bird_select_box')
        st.write("You selected: ", bird_file_returned)


        if bird_file_returned is None:
            st.write("")
        else:
            # download file from s3 bucket
            s3 = boto3.client('s3')
            bird_response = s3.get_object(Bucket=returned_bird_s3_bucket_name, Key=bird_file_returned)
            bird_file_stream = BytesIO(bird_response['Body'].read())

            st.image(bird_file_stream)

        returned_fish_s3_bucket_name = 'returned-fish-photos'

        # select file from s3 bucket
        s3 = boto3.client('s3')
        fish_response = s3.list_objects_v2(Bucket=returned_fish_s3_bucket_name)

        fish_file_list = []
        # Check if there are any items in the s3 bucket, if there are, add them to the file_list, if there aren't display a message
        if 'Contents' in fish_response:
            for obj in fish_response['Contents']:
                fish_file_list.append(obj['Key'])
        else:
            st.write("No files in fish S3 bucket")

        fish_file_returned = st.selectbox("View fish Photos Uploaded", fish_file_list, placeholder="Select a file from S3 bucket", index=None, key='fish_select_box')
        st.write("You selected: ", fish_file_returned)


        if fish_file_returned is None:
            st.write("")
        else:
            # download file from s3 bucket
            s3 = boto3.client('s3')
            fish_response = s3.get_object(Bucket=returned_fish_s3_bucket_name, Key=fish_file_returned)
            fish_file_stream = BytesIO(fish_response['Body'].read())

            st.image(fish_file_stream)


        returned_reptile_s3_bucket_name = 'returned-reptile-photos'

        # select file from s3 bucket
        s3 = boto3.client('s3')
        reptile_response = s3.list_objects_v2(Bucket=returned_reptile_s3_bucket_name)

        reptile_file_list = []
        # Check if there are any items in the s3 bucket, if there are, add them to the file_list, if there aren't display a message
        if 'Contents' in reptile_response:
            for obj in reptile_response['Contents']:
                reptile_file_list.append(obj['Key'])
        else:
            st.write("No files in reptile S3 bucket")

        reptile_file_returned = st.selectbox("View reptile Photos Uploaded", reptile_file_list, placeholder="Select a file from S3 bucket", index=None, key='reptile_select_box')
        st.write("You selected: ", reptile_file_returned)


        if reptile_file_returned is None:
            st.write("")
        else:
            # download file from s3 bucket
            s3 = boto3.client('s3')
            reptile_response = s3.get_object(Bucket=returned_reptile_s3_bucket_name, Key=reptile_file_returned)
            reptile_file_stream = BytesIO(reptile_response['Body'].read())

            st.image(reptile_file_stream)