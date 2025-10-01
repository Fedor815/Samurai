def generate_greeting(student):
    current_year = 2024
    years_studying = current_year - student['admission_year'] + 1
    
    greeting = f"\n🎓 Добро пожаловать, {student['full_name']}!"
    greeting += f"\n{'='*50}"
    greeting += f"\n📊 Ваши образовательные метрики:"
    greeting += f"\n├─ 🏫 Колледж: {student['college']}"
    greeting += f"\n├─ 👥 Группа: {student['group']}"
    greeting += f"\n├─ 📅 Год поступления: {student['admission_year']}"
    greeting += f"\n├─ 📚 Текущий курс: {student['course']}"
    greeting += f"\n└─ ⏱️ Лет обучения: {years_studying}"
    
    if student['course'] == 1:
        greeting += f"\n\n🌟 Вы только начинаете свой образовательный путь!"
    elif student['course'] >= 3:
        greeting += f"\n\n🎯 Вы уже опытный студент! Скоро диплом!"
    
    return greeting

def display_student_info(student):
    greeting = generate_greeting(student)
    print(greeting)

def register_new_student(full_name, students, filename):
    print(f"\n❌ Студент {full_name} не найден в базе.")
    response = input("Хотите зарегистрироваться? (да/нет): ").lower().strip()
    
    if response == 'да':
        try:
            print("\n📝 Регистрация нового студента:")
            group = input("Введите учебную группу: ")
            college = input("Введите название колледжа: ")
            admission_year = int(input("Введите год поступления: "))
            course = int(input("Введите текущий курс: "))
            
            if admission_year < 2000 or admission_year > 2024:
                print("❌ Ошибка: Некорректный год поступления")
                return None
            if course < 1 or course > 6:
                print("❌ Ошибка: Некорректный номер курса")
                return None
            
            new_student = {
                'full_name': full_name,
                'group': group,
                'college': college,
                'admission_year': admission_year,
                'course': course
            }
            students.append(new_student)
            
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(f"\n| {full_name} | {group} | {college} | {admission_year} | {course} |")
            
            print("✅ Студент успешно зарегистрирован!")
            return new_student
            
        except ValueError:
            print("❌ Ошибка: Введите корректные числовые значения")
        except Exception as e:
            print(f"❌ Ошибка при регистрации: {e}")
    
    return None