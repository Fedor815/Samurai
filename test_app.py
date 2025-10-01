import pytest
from app import generate_greeting, register_new_student

class TestGreetingLogic:
    def test_generate_greeting_contains_all_metrics(self):
        test_student = {
            'full_name': 'Тестовый Студент',
            'group': 'ТЕСТ-101',
            'college': 'Тестовый колледж',
            'admission_year': 2023,
            'course': 2
        }
        
        greeting = generate_greeting(test_student)
        assert test_student['full_name'] in greeting
        assert test_student['group'] in greeting
        assert test_student['college'] in greeting
        assert str(test_student['admission_year']) in greeting
        assert str(test_student['course']) in greeting
        assert 'Лет обучения' in greeting