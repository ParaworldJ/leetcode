import requests,json
from datetime import datetime,timedelta
urlPbm = 'https://gv.helloword.cn/api/v3/grammar/student/template/raw_data?tplid=60365928e154a73b798b4583&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MjM4MDc1MzQsImp0aSI6ImExMjM0NTY3ODkiLCJpc3MiOiJIZWxsb1dvcmQiLCJuYmYiOjE2MjM4MDc1MzQsImV4cCI6MTYyMzg5MzkzNCwiZGF0YSI6eyJ1c2VySWQiOiI1YjM3NGJkNDUzNjI3NjY4NzI4YjQ1ZmEiLCJ1c2VybmFtZSI6InRlc3QwNSJ9fQ.5htUwI5jCZvctIBOjpmOt02H1tcERnxbQT7DyJ1QDXcV-Z258gogmRRkaywPG8b2id1-CUpG4KoZvvTyIFfiNQ&error=1'
urlStd = 'https://gv.helloword.cn/api/v3/grammar/student/template/answer?stplid=60365930e154a739798b458a&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MjM4MDc1MzQsImp0aSI6ImExMjM0NTY3ODkiLCJpc3MiOiJIZWxsb1dvcmQiLCJuYmYiOjE2MjM4MDc1MzQsImV4cCI6MTYyMzg5MzkzNCwiZGF0YSI6eyJ1c2VySWQiOiI1YjM3NGJkNDUzNjI3NjY4NzI4YjQ1ZmEiLCJ1c2VybmFtZSI6InRlc3QwNSJ9fQ.5htUwI5jCZvctIBOjpmOt02H1tcERnxbQT7DyJ1QDXcV-Z258gogmRRkaywPG8b2id1-CUpG4KoZvvTyIFfiNQ&error=1'
responsePbm = requests.get(urlPbm)
responseStd = requests.get(urlStd)
dataPbm = responsePbm.json()
dataStd = responseStd.json()
stdkeyfront = 'real-60365930e154a739798b458a-'
for Procedure in dataPbm['data']['RawData']['ProcedureList']:
    Procedurename = Procedure['Name']
    if Procedurename == '本节课打卡':
        break
    print(Procedurename)
    for Task in Procedure['TaskList']:
        TaskNo = Task['Task']['No']
        TaskId = Task['Task']['TaskId']
        if Procedurename == '单项选择':
            num = '1'
            startTimeint = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['startTime']
            endTimeint = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['endTime']
            subTimeint= dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['submitTime'] 
            startT = datetime.fromtimestamp(startTimeint // 1000)
            subT = datetime.fromtimestamp(subTimeint // 1000)
            endT = datetime.fromtimestamp(endTimeint // 1000)
            if subTimeint == 0 and endTimeint == 0:
                E1 = '未提交'
                E2 = str(int((endT - subT).total_seconds()))+'秒'
            elif subTimeint > 0 and endTimeint == 0:
                E1 = '选择过'
                E2 = '未提交'
            else:
                E1 = str(int((subT - startT).total_seconds()))+'秒'
                E2 = str(int((endT - subT).total_seconds()))+'秒'
        elif Procedurename == '词转刷题':
            num = '2'
            startTimeint = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['startTime']
            endTimeint = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['endTime']
            subTimeint= dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['submitTime'] 
            startT = datetime.fromtimestamp(startTimeint // 1000)
            subT = datetime.fromtimestamp(subTimeint // 1000)
            endT = datetime.fromtimestamp(endTimeint // 1000)
            if subTimeint == 0 and endTimeint == 0:
                E1 = '未提交'
                E2 = str(int((endT - subT).total_seconds()))+'秒'
            elif subTimeint > 0 and endTimeint == 0:
                E1 = '选择过'
                E2 = '未提交'
            else:
                E1 = str(int((subT - startT).total_seconds()))+'秒'
                E2 = str(int((endT - subT).total_seconds()))+'秒'
        elif Procedurename == '首字母填空':
            num = '3'
            startTimeint = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['startTime']
            endTimeint = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['endTime']
            subTimeint= dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['submitTime'] 
            startT = datetime.fromtimestamp(startTimeint // 1000)
            subT = datetime.fromtimestamp(subTimeint // 1000)
            endT = datetime.fromtimestamp(endTimeint // 1000)
            if subTimeint == 0 and endTimeint == 0:
                E1 = '未提交'
                E2 = str(int((endT - subT).total_seconds()))+'秒'
            elif subTimeint > 0 and endTimeint == 0:
                E1 = '选择过'
                E2 = '未提交'
            else:
                E1 = str(int((subT - startT).total_seconds()))+'秒'
                E2 = str(int((endT - subT).total_seconds()))+'秒'
        elif Procedurename == '句转刷题':
            num = '4'
            startTimeint = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['startTime']
            endTimeint = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['endTime']
            subTimeint= dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['submitTime'] 
            startT = datetime.fromtimestamp(startTimeint // 1000)
            subT = datetime.fromtimestamp(subTimeint // 1000)
            endT = datetime.fromtimestamp(endTimeint // 1000)
            if subTimeint == 0 and endTimeint == 0:
                E1 = '未提交'
                E2 = str(int((endT - subT).total_seconds()))+'秒'
            elif subTimeint > 0 and endTimeint == 0:
                E1 = '选择过'
                E2 = '未提交'
            else:
                E1 = str(int((subT - startT).total_seconds()))+'秒'
                E2 = str(int((endT - subT).total_seconds()))+'秒'
        elif Procedurename == '句子翻译':
            num = '5'
            startTimeint = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['startTime']
            endTimeint = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['endTime']
            subTimeint= dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['submitTime'] 
            startT = datetime.fromtimestamp(startTimeint // 1000)
            subT = datetime.fromtimestamp(subTimeint // 1000)
            endT = datetime.fromtimestamp(endTimeint // 1000)
            if subTimeint == 0 and endTimeint == 0:
                E1 = '未提交'
                E2 = str(int((endT - subT).total_seconds()))+'秒'
            elif subTimeint > 0 and endTimeint == 0:
                E1 = '选择过'
                E2 = '未提交'
            else:
                E1 = str(int((subT - startT).total_seconds()))+'秒'
                E2 = str(int((endT - subT).total_seconds()))+'秒'
        print('第',TaskNo,'题',' ',
            E1,' ',
            E2
            )