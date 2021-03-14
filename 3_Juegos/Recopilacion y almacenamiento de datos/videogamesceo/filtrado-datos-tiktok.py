import pandas as pd
dataframe1 = pd.read_csv('videogamesceo_1609806891401.csv')
temp_dataframe1 = dataframe1.append(dataframe1)
temp_dataframe2 = temp_dataframe1.drop(['authorMeta.id', 'authorMeta.secUid', 'authorMeta.name', 'authorMeta.nickName', 'authorMeta.verified',"authorMeta.signature","authorMeta.avatar","musicMeta.musicId","musicMeta.musicAuthor","musicMeta.musicOriginal","musicMeta.playUrl","musicMeta.coverThumb","musicMeta.coverMedium","musicMeta.coverLarge","covers.default","covers.origin","covers.dynamic","webVideoUrl","videoUrlNoWaterMark","videoMeta.height","videoMeta.width","diggCount","mentions"], axis=1)
temp_dataframe2.to_csv("Tik-Tok-filtrado.csv")