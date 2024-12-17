# библиотека для работы с json
import json

# переменная skills, булевое значение , если нашло профессию , то выведет результат
skills=False

# запрос на ввод id у пользователя
num=str(input("Введите номер квалификации : "))

# читаем файл
with open("dump.json","r",encoding="utf-8") as file:
    doc=json.load(file)

# блок кода на наличие профессии
for skill in doc:
    if skill.get("model") == "data.skill" :
        if skill["fields"].get("code") == num :
            code=skill["fields"].get("code")
            title=skill["fields"].get("title")
            skills=True

          # если нашло профессию , то этот блок кода ищет специальность
            for specialty in doc :
                if specialty.get("model") == "data.specialty" :
                    specialty_code= specialty["fields"].get("code")
                    if specialty_code in code :
                        specialty_title = specialty["fields"].get("title")
                        specialty_type = specialty["fields"].get("c_type")

# блок кода вывода
if skills == True :
    print("============================== Найдено ==============================")
    print(f"{specialty_code} >> Специалность '{specialty_title}' , {specialty_type} ")
    print(f"{code} >> квалификация '{title}'")
# блок кода исключения
else :
    print("=============== Не найдено ===============")
