from django.db import models

# Create your models here.

"""活動名稱"""
class Activity(models.Model):
    name = models.CharField(max_length=80)
    #name = db.Column(db.String(80), nullable=False)

    #全部社課
    @classmethod
    def get_all_activity_list(cls):
        return cls.query.all()

"""
一個 Activity 有多個 Member，一對多的關係
"""

"""活動成員"""
class Member(models.Model):
    name = models.CharField(max_length=80) #姓名
    nid = models.CharField(max_length=10) #學號
    department = models.CharField(max_length=20) #系級(ex.資訊一甲)
    sex = models.CharField(max_length=1) #性別
    birthday = models.CharField(max_length=20) #出生年月日(ex.1999/09/09)
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)

    #單一社課人數總和
    @classmethod
    def get_activity_member_count(cls, id):
        return cls.query.filter_by(activity_id=id).count()
    #單一社課全部資料
    @classmethod
    def get_activity_member(cls, id):
        return cls.query.filter_by(activity_id=id).all()
    #單一社課男女人數
    @classmethod
    def get_sex_number(cls, id):
        boy = cls.query.filter_by(activity_id=id, sex='男').count()
        girl = cls.query.filter_by(activity_id=id, sex='女').count()
        return [boy,girl]
    #單一社課年級人數
    @classmethod
    def get_level_number(cls, id):
        result = [0,0,0,0]
        for i in cls.query.filter_by(activity_id=id).all():
            if re.search(r'一', i.department):
                result[0] = result[0] + 1
            elif re.search(r'二', i.department):
                result[1] = result[1] + 1
            elif re.search(r'三', i.department):
                result[2] = result[2] + 1
            elif re.search(r'四', i.department):
                result[3] = result[3] + 1
        return result
    #單一社課各系人數
    @classmethod
    def get_department_number(cls, id):
        result = {}
        for i in cls.query.filter_by(activity_id=id).all():
            s = re.findall(r'[^一,二,三,四]*', i.department)[0]
            try:
                result[s] = result[s]+1
            except KeyError:
                result[s] = 1
        return result