import requests, json
url2 = 'https://gv.helloword.cn/api/v3/grammar/student/template/raw_data?tplid=60365857e154a7da6c8b46d5&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MjM1ODYyMTAsImp0aSI6ImExMjM0NTY3ODkiLCJpc3MiOiJIZWxsb1dvcmQiLCJuYmYiOjE2MjM1ODYyMTAsImV4cCI6MTYyMzY3MjYxMCwiZGF0YSI6eyJ1c2VySWQiOiI1YjM3NGJkNDUzNjI3NjY4NzI4YjQ1ZmEiLCJ1c2VybmFtZSI6InRlc3QwNSJ9fQ.egYSeSBtQbQeuvoNlITyda6WENdPSnBGucbI0G2aueuaK8YsvTfOTTuBuupWrNQQsb1lIlqFxhAywxKC6gcYQQ&error=1'
url = 'https://gv.helloword.cn/api/v3/grammar/student/template/answer?stplid=6036585de154a7da6c8b46d8&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MjM1ODYyMTAsImp0aSI6ImExMjM0NTY3ODkiLCJpc3MiOiJIZWxsb1dvcmQiLCJuYmYiOjE2MjM1ODYyMTAsImV4cCI6MTYyMzY3MjYxMCwiZGF0YSI6eyJ1c2VySWQiOiI1YjM3NGJkNDUzNjI3NjY4NzI4YjQ1ZmEiLCJ1c2VybmFtZSI6InRlc3QwNSJ9fQ.egYSeSBtQbQeuvoNlITyda6WENdPSnBGucbI0G2aueuaK8YsvTfOTTuBuupWrNQQsb1lIlqFxhAywxKC6gcYQQ&error=1'
response = requests.get(url)
responseTG = requests.get(url2)
text = response.text
data = response.json()
dataTG = responseTG.json()
# print(dataTG['data'].keys())
for Procedure in dataTG['data']['RawData']['ProcedureList']:
    if Procedure['Name'] == '语法单选':
        for Task , Value in zip(Procedure['TaskList'],sorted(data['data']['StudentTemplateAnswer'].items())): #有点投机
            if Value[1]['real-page-state']['taskState']['result']['stdAnswer'] == '':
                StuAnswer = ' '
            else:
                StuAnswer = Value[1]['real-page-state']['taskState']['result']['userAnswer']
            print('第',Task['Task']['TaskId'][-2 : ],'题' ,' ', 
                StuAnswer ,' ',
                Task['Task']['Choice']['AnswerId'] ,' ',
                Value[1]['real-page-state']['taskState']['userScore'] ,' ',
                Task['Task']['Choice']['Stem']
                )

           # print(Value[1]['real-page-state']['taskState']['result']['stdAnswer'] )
    # for Task in Procedure['TaskList']:

    #     print(Task['Task']['TaskId'], Task['Task']['Choice']['Stem'])

# print(json.dumps(data, indent = 4, ensure_ascii = True, sort_keys = True))
# for key, value in data['data']['StudentTemplateAnswer'].items() :
#     result = value['real-page-state']['taskState']['result']
#     print(key, result['stdAnswer'], result['userAnswer'])