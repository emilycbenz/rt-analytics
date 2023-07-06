import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime
from helper_function import replace_number_with_name
import streamlit as st

users_df = pd.read_pickle('Cleaned Data/export_All-Users.pkl')
communities_df = pd.read_pickle('Cleaned Data/export_All-Communities.pkl')
nonadmin_users_df = pd.read_pickle('Cleaned Data/nonadmin_users.pkl')
posts_df = pd.read_pickle('Cleaned Data/export_All-Posts.pkl')
comments_df = pd.read_pickle('Cleaned Data/export_All-t-Comments.pkl')
nonadmin_users_df = pd.read_pickle('Cleaned Data/nonadmin_users.pkl')
just_posts_df = pd.read_pickle('Cleaned Data/just_posts.pkl')
resources_df = pd.read_pickle('Cleaned Data/export_All-Resources.pkl')

selected_community = st.selectbox('Select a Community', communities_df['Name'].sort_values())

# User-Community Dataframe expansion
users_df['Communities List'] = users_df['Communities'].str.split(',')
user_community_df = users_df.explode('Communities List')
user_community_df['Communities List'] = user_community_df['Communities List'].str.strip()

posts_df = posts_df[(posts_df['Community'] == selected_community)]
users_df = user_community_df[user_community_df['Communities List'] == selected_community]
nonadmin_users_df = users_df[users_df['User_Type'] == 'User']
comments_df = comments_df[comments_df['Community'] == selected_community]
resources_df = resources_df[resources_df['Community'] == selected_community]
just_posts_df = just_posts_df[just_posts_df['Community'] == selected_community]
resources_df = resources_df[resources_df['Community'] == selected_community]

admin_names = list(users_df[users_df['User_Type'] == 'Admin']['email'])

total_onboarded_nonadmin_users = nonadmin_users_df.count()['Onboarding completed']
total_posts = posts_df[posts_df['Type'] == 'Post'].count()['unique id']
total_polls = posts_df[posts_df['Type'] == 'Poll'].count()['unique id']

st.write(f"There are a total of {total_onboarded_nonadmin_users} users in the platform and {total_posts + total_polls} posts and\
 {len(resources_df)} resources uploaded.")

#st.line_chart(data=users_per_month, x='Sorting_Year_Month',
#              y='New_Users')