import json

json_data = '''
{
    "mentor": {
        "Name" : "Tom",
        "Age" : 20
    },
    "mentee" : {
        "Name" : "Eric",
        "Age" : 13
    }
}
'''
# JSON 파일을 읽을 때는 json.load(파일 객체)를 사용, 딕셔너리 자료형을 JSON 파일로 생성할 때는 다음처럼 json.dump(딕셔너리, 파일 객체)를 사용
# json.loads() : json데이터 파징
json_obj = json.loads(json_data)

print(json_obj) # {'mentor': {'Name': 'Tom', 'Age': 20}, 'mentee': {'Name': 'Eric', 'Age': 13}}
print("Mentor : " + json_obj['mentor']['Name'])
print("Mentee : " + json_obj['mentee']['Name'])

what = [{'user': '더미', 'content': '개인 프로젝트라고 해도 크롤링은 답이 아닙니다.', 'createAt': '3일전'}, {'user': '삶은개발', 'content': '데이터 취급은 항상 중요하긴 하죠\n공개 비공개 확인 잘 해보시고 활용해 보시길 바랍니다.\n어떤 데이터 입수처가 좋을까요', 'createAt': '3일전'}]
print(json.dumps(what))
# ASCII가 아닌 문자 유지
print(json.dumps(what, ensure_ascii=False))
print(json.loads(json.dumps(what)))


# asd = [{'user': '더미', 'content': '회사마다 다릅니다', 'createAt': '5일전'}
#        , {'user': 'xml개발자', 'content': ""업계마다 달라서 정답이 없습니다.\n만약 경력 산정을하는 업계라면.. 대학 졸업하기 전의 경력은 '고졸의 경력'으로 취급됩니다.\n하는 일은 똑같은 데, '고졸 시절의 경력은 고졸이 할만한 일이다.'라는 논리로 억까당할 수 있습니다.\n학교 선배들이나 회사 사람들과 이야기해보시는 게 좋을 것 같습니다."", 'createAt': '5일전'}, {'user': '프레이야', 'content': '잘 협의만 되면 가능하기도 하니 잘 말씀드려 보세여.', 'createAt': '5일전'}, {'user': 'Bugfix', 'content': '그냥저냥 경력쌓고 건축사 취득 하실거면 적당한곳 가셔서 1년이라도 경력 빨리 쌓는게 좋구요.\nTV 에서 보는 건축 디자인 설계를 하고 싶으신 경우 유럽쪽으로 유학을 갔다오는게 좋습니다.\n일반적인 경우 설계쪽으로는 일반 설계 회사 들어가서는 TV 에서 보는 멋있는 설계하고 그런 기회가 잘 안생깁니다.', 'createAt': '5일전'}, {'user': '옴뇸뇸뇸', 'content': '저요 취업 안될까바 졸유했는데 운좋게 취업이 돼서 정신없이 회사다니다가\n졸업 요건을 못 맞춰서 강제 졸유 한 학기 더하고 회사 다니고 있네요', 'createAt': '5일전'}]