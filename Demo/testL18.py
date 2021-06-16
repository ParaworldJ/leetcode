import requests, json
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
            TaskStem = Task['Task']['Choice']['Stem'][0 : 50]
            TaskAnswerId = Task['Task']['Choice']['AnswerId']
            StdAnswer = ''
            if stdkeyfront + num + '-' + TaskId not in dataStd['data']['StudentTemplateAnswer'].keys() or dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['taskState']['result']['userAnswer'] == '':
                StdAnswer = ' '
            else:
                StdAnswer = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['taskState']['result']['userAnswer']
        elif Procedurename == '词转刷题':
            num = '2'
            TaskStem = Task['Task']['Completion']['Stem'][0][0 : 50]
            TaskAnswerId = Task['Task']['Completion']['Blanks'][0]['Answer']
            StdAnswer = ''
            if stdkeyfront + num + '-' + TaskId not in dataStd['data']['StudentTemplateAnswer'].keys() or dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['taskState']['result']['userAnswer'] == '':
                StdAnswer = '\t '
            else:
                StdAnswer = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['taskState']['result']['userAnswer'][0][0]
        elif Procedurename == '首字母填空':
            num = '3'
            TaskStem = Task['Task']['Completion']['Stem'][0][0 : 50]
            TaskAnswerId = Task['Task']['Completion']['Blanks'][0]['Answer']
            StdAnswer = ''
            if stdkeyfront + num + '-' + TaskId not in dataStd['data']['StudentTemplateAnswer'].keys() or dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['taskState']['result']['userAnswer'] == '':
                StdAnswer = ' \t'
            else:
                StdAnswer = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['taskState']['result']['userAnswer'][0][0]
        elif Procedurename == '句转刷题':
            num = '4'
            TaskStem = ''
            TaskAnswerId = ''
            StdAnswer = ''
            if stdkeyfront + num + '-' + TaskId not in dataStd['data']['StudentTemplateAnswer'].keys() or dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['taskState']['result']['userAnswer'] == '':
                StdAnswer = ' '
            else:
                StdAnswertemp = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['taskState']['result']['userAnswer'][0]
                for StdAnswernum in range(len(StdAnswertemp)):
                    if StdAnswernum == 0:
                        if StdAnswertemp[StdAnswernum] == '':
                            StdAnswertemp[StdAnswernum] = '\t'
                        StdAnswer = StdAnswertemp[StdAnswernum]
                    else:
                        if StdAnswertemp[StdAnswernum] == '':
                            StdAnswertemp[StdAnswernum] = '\t'   
                        StdAnswer = StdAnswer + ',' + StdAnswertemp[StdAnswernum]
            for TStem in Task['Task']['Completion']['Stem']:
                TaskStem = TaskStem + ' ' + TStem
            for TAnswerId in Task['Task']['Completion']['Blanks']:
                TaskAnswerId =TaskAnswerId + ' ' + TAnswerId['Answer']
            TaskStem = TaskStem[0 : 50]
        elif Procedurename == '句子翻译':
            num = '5'
            TaskStem = ''
            TaskAnswerId = ''
            if stdkeyfront + num + '-' + TaskId not in dataStd['data']['StudentTemplateAnswer'].keys() or dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['taskState']['result']['userAnswer'] == '':
                StdAnswer = ' '
            else:
                StdAnswer = dataStd['data']['StudentTemplateAnswer'][stdkeyfront + num + '-' + TaskId]['real-page-state']['taskState']['result']['userAnswer'][0][0]
            for TStem in Task['Task']['Completion']['Stem']:
                TaskStem = TaskStem + ' ' + TStem
            for TAnswerId in Task['Task']['Completion']['Blanks']:
                TaskAnswerId =TaskAnswerId + ' ' + TAnswerId['Answer']
            TaskStem = TaskStem[0 : 50]
        print('第',TaskNo,'题',' ',
            StdAnswer,' ',
            TaskAnswerId,' ',
            TaskStem,' ',
            
            )