import xml.etree.ElementTree as ET

person = ET.Element("Person")

name = ET.Element("name")
name.text = "Thomas Shelby"
person.append(name)  # name 태그를 person 태그에 append

age = ET.Element("age")
age.text = "34"
person.append(age)  # age 태그를 person 태그에 append

ET.SubElement(person, "place").text = "Birmingham"  # 자식 태그 생성

person.attrib["id"] = "0x0001"  # person의 attribute 변경
name.tag = "fullName"  # name의 태그명 변경

# 새로운 태그 생성
gang = ET.Element("gangName", loc="England")
gang.text = "Peaky Blinders"

# name 태그 다음 위치에 삽입
person.insert(1, gang)

# 태그 삭제
person.remove(age)


ET.dump(person)  # sys.stdout
ET.ElementTree(person).write("person.xml")  # 파일로 저장

