from typing import Dict, Tuple, Any, List

class StudentProfile:
    """Talaba profili - barcha atributlar yopiq, faqat API orqali boshqariladi."""

    def __init__(self, name: str, group: str):
        self.__name = name
        self.__group = group
        self.__grades: List[int] = []
        self.__metadata: Dict[str, Any] = {}

    @property
    def name(self) -> str:
        return self.__name

    @property
    def group(self) -> str:
        return self.__group

    @property
    def gpa(self) -> float:
        if not self.__grades:
            return 0.0
        normalized = [(g - 1) / 4 for g in self.__grades]  
        avg = sum(normalized) / len(normalized)

        return round(avg * 4, 2)

    def add_grade(self, grade: int) -> None:
        if not (1 <= grade <= 5):
            raise ValueError("Baho 1-5 oralig'ida bo'lishi kerak.")
        self.__grades.append(grade)

    def get_grades(self) -> Tuple[int, ...]:
        return tuple(self.__grades)

    def add_meta(self, key: str, value: Any) -> None:
        self.__metadata[key] = value

    def get_meta(self) -> Dict[str, Any]:
        return dict(self.__metadata)


class GradeBook:
    def __init__(self, semester: str):
        self.semester = semester
        self.__students: Dict[str, StudentProfile] = {}
        self.__current_student: StudentProfile | None = None
        self.__logs: List[str] = []

    def log(self, msg: str):
        self.__logs.append(msg)

    def get_logs(self) -> Tuple[str, ...]:
        return tuple(self.__logs)

    def create_or_get(self, name: str, group: str) -> StudentProfile:
        if name not in self.__students:
            self.__students[name] = StudentProfile(name, group)
            self.log(f"Talaba yaratildi: {name}")
        self.__current_student = self.__students[name]
        return self.__current_student

    def select(self, name: str):
        if name not in self.__students:
            raise KeyError("Bunday talaba yo'q.")
        self.__current_student = self.__students[name]

    def get_students(self) -> Tuple[StudentProfile, ...]:
        return tuple(self.__students.values())

    def add_grade(self, grade: int) -> None:
        if not self.__current_student:
            raise RuntimeError("Talaba tanlanmagan.")
        self.__current_student.add_grade(grade)
        self.log(f"Baho qo'shildi: {grade} → {self.__current_student.name}")

    def set_gpa(self, name: str, value: float):
        self.log("GPA qo'lda o'rnatish endi ishlamaydi (avtomatik).")

    def print_report(self):
        print(f"SEMESTR: {self.semester}")
        for student in self.__students.values():
            print(
                f"{student.name} ({student.group}) → "
                f"GPA: {student.gpa}, Grades: {student.get_grades()}"
            )


class AccessControlledGradeBook(GradeBook):
    """Huquq darajasiga ko'ra cheklangan GradeBook."""

    def __init__(self, semester: str, access_level: str):
        super().__init__(semester)
        self.__access = access_level.lower()

    def add_grade(self, grade: int):
        if self.__access not in ("admin", "teacher"):
            self.log("Ruxsat yo'q: baho qo'shish bloklandi")
            return
        super().add_grade(grade)

    def set_gpa(self, name: str, value: float):
        self.log(f"GPA avtomatik, qo'lda o'zgartirilmaydi: {name}")


def demo():
    gb = AccessControlledGradeBook("Fall 2025", "teacher")

    gb.create_or_get("Ali", "CS-202")
    gb.add_grade(2)
    gb.add_grade(5)

    gb.create_or_get("Laylo", "CS-202")
    gb.add_grade(5)
    gb.add_grade(4)

    gb.print_report()
    print("\nLOG:", gb.get_logs())


if __name__ == "__main__":
    demo()
