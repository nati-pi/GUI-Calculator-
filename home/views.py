from django.shortcuts import render
from django.http import HttpResponse
from .models import File


def home(request):
    return render(request, 'index.html')


def calc(request):
    global ma, ph, ci, en, c
    red = 0
    math = request.GET['math']
    civic = request.GET['civic']
    english = request.GET['english']
    cse = request.GET['cse']
    td = request.GET['td']
    physics = request.GET['physics']
    outfile = open('file.txt', 'w')
    outfile.write("This is your complete data of your total GPA results the approprate letters beside your mark is the respective grade for each subject\n")
    outfile.write("this web page is designed in 2021/1/29GC contact the developers on telegram @space_blank for more information.\n\n")
    subj = [math, civic, english, cse, td, physics]
    desc = []
    for i in range(len(desc)):
        outfile.write("\t"+desc[i]+"\t\t")
    outfile.write("\n")
    outfile.write("Maths\t\tCivic\t\tEnglish\t\tCSE\t\tTD\t\tPhysics\n")
    sum = 0
    grade = []
    value = []
    for i in range(len(subj)):
        convert = int(subj[i])
        if convert >= 90:
            grade.append('A+')
            subj[i] = '4'
            value.append(subj[i])
        elif convert>=85:
            grade.append('A')
            subj[i] = '4'
            value.append(subj[i])
        elif convert >= 80:
            grade.append('A-')
            subj[i] = '3.75'
            value.append(subj[i])
        elif convert >=75:
            grade.append('B+')
            subj[i] = '3.5'
            value.append(subj[i])
        elif convert>= 60:
            grade.append('B')
            subj[i] = '3'
            value.append(subj[i])
        elif convert>=40:
            grade.append('C')
            subj[i] = '2'
            value.append(subj[i])
        elif convert>=30:
            grade.append('D')
            subj[i] = '1'
            value.append(subj[i])
        else:
            grade.append('F')
            subj[i] = '0'
            value.append(subj[i])
        sum = format((float(subj[0])*4 + float(subj[1])*3 + float(subj[2])*3 + float(subj[3])*3 + float(subj[4])*3 + float(subj[5])*3)/19,"10.2F")
    if float(sum) >= 1.5:
        sum = sum
    else:
        red = sum
    mathv = value[0]
    phyv = value[1]
    civv = value[2]
    engv = value[3]
    csev = value[4]
    tdv = value[5]
    ma = grade[0]
    ph = grade[1]
    ci = grade[2]
    en = grade[3]
    c = grade[4]
    t = grade[5]
    context = {
        'red': red,
        'mathv':mathv,
        'phyv': phyv,
        'civv': civv,
        'engv': engv,
        'csev': csev,
        'tdv': tdv,
        'sum': sum,
        'math': math,
        'physics': physics,
        'civic': civic,
        'english': english,
        'cse': cse,
        'td': td,
        'ma': ma,
        'ph': ph,
        'ci': ci,
        'en': en,
        'c': c,
        't': t

    }
    return render(request, 'second.html', context)


def another(request):
    mat = request.GET['mat']
    eng = request.GET['eng']
    civ = request.GET['civ']
    che = request.GET['che']
    phy = request.GET['phy']
    cs = request.GET['cs']
    subj = [mat, eng, civ, che, phy, cs]
    sum = 0
    grade = []
    value = []
    for i in range(len(subj)):
        convert = int(subj[i])
        if convert >= 90:
            grade.append('A+')
            subj[i] = '4'
            value.append(subj[i])
        elif convert >= 85:
            grade.append('A')
            subj[i] = '4'
            value.append(subj[i])
        elif convert >= 80:
            grade.append('A-')
            subj[i] = '3.75'
            value.append(subj[i])
        elif convert >= 75:
            grade.append('B+')
            subj[i] = '3.5'
            value.append(subj[i])
        elif convert >= 60:
            grade.append('B')
            subj[i] = '3'
            value.append(subj[i])
        elif convert >= 40:
            grade.append('C')
            subj[i] = '2'
            value.append(subj[i])
        elif convert >= 30:
            grade.append('D')
            subj[i] = '1'
            value.append(subj[i])
        else:
            grade.append('F')
            subj[i] = '0'
            value.append(subj[i])
        sum = format((float(subj[0]) * 4 + float(subj[1]) * 3 + float(subj[2]) * 3 + float(subj[3]) * 3 + float(
            subj[4]) * 3 + float(subj[5]) * 3) / 19, "10.2F")

    mathv = value[0]
    phyv = value[1]
    civv = value[2]
    engv = value[3]
    csev = value[4]
    tdv = value[5]
    ma = grade[0]
    ph = grade[1]
    ci = grade[2]
    en = grade[3]
    c = grade[4]
    t = grade[5]
    context = {
        'mathv': mathv,
        'phyv': phyv,
        'civv': civv,
        'engv': engv,
        'csev': csev,
        'tdv': tdv,
        'sum': sum,
        'mat': mat,
        'phy': phy,
        'civ': civ,
        'che': che,
        'eng': eng,
        'cs': cs,
         'ma': ma,
        'ph': ph,
        'ci': ci,
        'en': en,
        'c': c,
        't': t
    }
    return render(request, 'first.html', context)


def cgpa(request):
    return render(request, 'gpa.html')