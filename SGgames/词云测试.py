
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator,STOPWORDS
import jieba
import csv
from os import path

text_path = '6ye.csv'
with open(text_path,'r',encoding="utf-8") as f:
    reader=csv.DictReader(f)
    text=[row["comment"]for row in reader]

x="".join(text)    #  导入的字符


image_colors = imread(r"3.png")  #mask地址
#image_colors = ImageColorGenerator(alice_coloring) mask地址
# 设置词云属性
wc = WordCloud(font_path=r"‪C:\Windows\Fonts\FZYTK.TTF",  # 设置字体
               background_color="white",  # 背景颜色
               max_words=500,  # 词云显示的最大词数
               mask=image_colors,  # 设置背景图片
               max_font_size=150,  # 字体最大值
               random_state=42,
                stopwords=STOPWORDS.add("发表"),
              # width=1000, height=860, margin=2,# 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
               )
list=["峰哥","YYF","yyf","傻狗","狗头","萨特","哭哭惹","虎扑","nga","rua","不喜欢"]
def add_word(list):
    for items in list:
        jieba.add_word(items)
add_word(list) #添加特殊词库

def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    with open('屏蔽词,txt',"r",encoding="utf-8") as f:
        str_text = f.read()
         # 把str格式转成unicode格式
        f.close()  # stopwords文本中词的格式是'一词一行'
    for word in word_generator:
        if word.strip() not in str_text:
            words_list.append(word)
    return ' '.join(words_list)  # 注意是空格
text = stop_words(x)

#wc.generate(text)


#wordlist_after_jieba = jieba.cut(x, cut_all=False)
#wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = wc.generate(text)

image_colors = ImageColorGenerator(image_colors)
# 显示图片
plt.imshow(my_wordcloud)
# 关闭坐标轴
plt.axis('off')
# 绘制词云
plt.figure()
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.axis('off')
# 保存图片
wc.to_file('2th.png')