import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns


st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # fetch unique users present in the conversation
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)
    if st.sidebar.button("Show analysis"):

        st.title("Chat Statistics")

        col1,col2,col3,col4 = st.columns(4)
        num_messages, words, media, links= helper.fetch_stats(selected_user,df)
        with col1:
            st.header("Total-Messages")
            st.title(num_messages)
        with col2:
            st.header("Total-Words")
            st.title(words)
        with col3:
            st.header("Total Media")
            st.title(media)
        with col4:
            st.header("Total Links")
            st.title(links)




        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, df1 = helper.most_busy_count(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:

                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation = 'vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(df1)

        # Monthly Timeline

        st.title("Monthly Timeline (One Year)")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'].tail(12), timeline['message'].tail(12), color="green")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        # Daily Timeline

        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeine(selected_user, df)
        plt.figure(figsize=(18, 10))
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['onlyDate'], daily_timeline['message'], color = "black")
        # ax.plot(daily_timeline['onlyDate'].tail(30),daily_timeline['message'].tail(30), color="black")

        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        # activity map
        st.title("Activity Map")
        col1, col2 = st.columns(2)
        with col1:
            st.header("Most Busy Day")
            week_map = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(week_map.index,week_map.values)
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        with col2:
            st.header("Most Busy Month")
            month_map = helper.monthly_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(month_map.index, month_map.values, color="orange")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        # heatmap

        st.header("Activity Map")
        user_activity = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_activity)
        st.pyplot(fig)



        # wordcloud

        st.title("WordCloud")
        df_wc = helper.create_wordcloud(selected_user,df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words

        st.title("Most Common Words")
        most_common_df = helper.most_common_word(selected_user, df)
        col1, col2 = st.columns(2)

        with col1:
            fig,ax = plt.subplots()

            ax.barh(most_common_df[0], most_common_df[1])
            plt.xticks(rotation = 'vertical')

            st.pyplot(fig)
        with col2:
            st.dataframe(most_common_df)

        # emoji analysis

        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df.head(20))
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct = "%0.2f")
            st.pyplot(fig)



















