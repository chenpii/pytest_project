class TestStudentName:
    def test_name(self, student):
        assert '小红' in student


class TestStudentScore:
    def test_name(self, student):
        assert student['小红'] > 90
