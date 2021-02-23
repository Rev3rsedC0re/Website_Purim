from flask import Flask, render_template, jsonify, request, flash, redirect, url_for, session
import json



app = Flask(__name__)
app.config['SECRET_KEY'] = 'u083hh+3fevjs9-dfjv9845guc98u98ufcu4usuf8ur88apidj98rmnrijfdj'
#app.config["SESSION_COOKIE_SECURE"] = True    ###on production###
#app.config["REMEMBER_COOKIE_HTTPONLY"] = True
#app.config["REMEMBER_COOKIE_SECURE"] = True

class Question:
    def __init__(self,title,opt1,opt2,opt3,opt4,correct):
        self.title = title
        self.opt1 = opt1
        self.opt2 = opt2
        self.opt3 = opt3
        self.opt4 = opt4
        self.correct = correct
    def __dict__(self):
        return {'title':title,'opt1':opt1,'opt2':opt2,'opt3':opt3,'opt4':opt4}
        

questions = [Question('איזה מדינה היא פרס כיום?',
                      'טורקיה',
                      'עיראק',
                      'איראן',
                      'אוזבקיסטן',
                      3),
             Question('מתי מרעישים ברעשן?',
                      'כאשר שמישהו נפצע.',
                      'כאשר מזכירים את שמו של המן',
                      'בבוקר ובערב פורים',
                      'בסיום חג פורים',
                      2),
             Question('איך קראו לשומרים שניסו להרעיל את המלך?',
                      'עופר ובגדן',
                      'תוריש והמן',
                      'פנחס ומרדכי',
                      'בגתן ותרש',
                      4),
             Question('איך קראו לאשתו של אחשוורוש לפני אסתר?',
                      'ושתי',
                      'מרים',
                      'רות',
                      'בת שבע',
                      1),
             Question('מה איים המן לעשות?',
                      'כל היהודים יגורשו מפרס',
                      'שומרי המלך ייקחו מכל היהודים את כל כספם ורכושם',
                      'כל היהודים יצאו להורג',
                      'יהיה אסור להתפלל ולעשות מצוות על פי התורה',
                      3),
             Question('מי היה מרדכי היהודי?',
                      'דוד של אסתר',
                      'אבא של אסתר',
                      'אח של אסתר',
                      'חבר של אבא של אסתר',
                      1),
             Question('השלם את המשפט: יִּקְרַע מָרְדֳּכַי אֶת בְּגָדָיו...',
                      'וילך לבשר לאסתר',
                      'וילבש שק אפר',
                      'ויסעד עד שבעו',
                      'ויתקלח כי ניצל הוא',
                      2),
             Question('מאיזה שבט הייתה משפחתו של מרדכי?',
                      'שבט כהן',
                      'שבט יהודה',
                      'שבט דן',
                      'שבט בנימין',
                      4),
             Question('גבולותיה של ממלכת פרס היו:',
                      'מאיראן עד מצרים',
                      'מהודו עד עיראק',
                      'מהודו עד כוש',
                      'מכוש עד ספרד ',
                      3),
             Question('מה היה הכינוי של המן?',
                      'המן האגגי',
                      'המן הפלישתי',
                      'המן העוכר',
                      'המן הרשע',
                      1)]
#6 אוזני המן

@app.route("/check", methods=["POST"])
def check():
    mistakes = []
    for i in range(len(questions)):
        if(int(request.form.get(str(i)))!=questions[i].correct):
            mistakes.append(questions[i].title)
    if(request.form.get('pic1_input')!='רעשן'):
        mistakes.append('מהו הפריט הקשור לפורים המסתתר בתמונה?')
    if(request.form.get('pic2_input')!='6'):
        mistakes.append('מצא כמה אוזני המן בתמונה')
    if(request.form.get('pic3_input')!='המלך'):
        mistakes.append('פתור את החידה')
    print(mistakes)
    if(len(mistakes)==0):
        return render_template("correct.html",h1='''כל הכבוד!
פתרתם את כל החידות נכון''',h2='הקוד הסודי הוא:',h3='משנכנס אדר מרבין בשמחה')
    return render_template("check.html",mistakes=mistakes,
                           title='אוי לא! לא הצלחת לפתור את כל החידות נכון. מזל שאת/ה תמיד יכול/ה לנסות שוב!',
                           sub='הטעויות שלך הן בשאלות:')

@app.route('/')
def main():
    return render_template("main.html",questions=questions,title='חידון פורים',
                           h1='מצא את האביזר הקשור לפורים הנמצא בתמונה',
                           h2='כמה אוזני המן יש בתמונה?',h3='פתור את החידה (קשה)',
                           p1='סמי הליצן שכח את הסיסמה שלו למנעול של התיבה בה הוא שומר את כל האביזרים שלו לפורים. עזרו לסמי למצוא את הקוד באמצעות פתרון כל השאלות')


if (__name__ == "__main__"):
    Flask.run(app,debug=True,use_reloader=False,host='10.0.0.17')



        
