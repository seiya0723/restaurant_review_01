from django.db import models

#カテゴリモデル(ここに店舗のカテゴリが格納される)
class Category(models.Model):

    name        = models.CharField(verbose_name="カテゴリ名",max_length=50) 



#店舗モデル(ここに店舗の情報が格納される)
class Restaurant(models.Model):

    name        = models.CharField(verbose_name="店名",max_length=50) 

    prefectures = models.CharField(verbose_name="都道府県",max_length=10)
    city        = models.CharField(verbose_name="市",max_length=50)
    address     = models.CharField(verbose_name="町・番地",max_length=200)


    #TODO:後に店舗の画像を指定するフィールドを作る(ImageField())
    #TODO:後に店舗のカテゴリを指定するフィールドを作る(1対多を意味するmodels.ForeignKey()を使用)
    #TODO:後に店舗のマップ位置(緯度と経度)を記録するフィールドを作る(FloatField()を使用する)


#(ここにレビュー情報が格納される)
class Review(models.Model):

    title       = models.CharField(verbose_name="タイトル",max_length=100)
    content     = models.CharField(verbose_name="本文",max_length=1000)

    #TODO:ここに星の上限と下限を指定する(例えば5つ星なら上限5、下限1など)
    #レビューの星を描画する方法 → https://noauto-nolife.com/post/django-template-integer-for-loop/
    #star        = models.IntegerField(verbose_name="星の数")








