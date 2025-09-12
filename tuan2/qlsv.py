from __future__ import annotations  # an toàn cho type hint (tùy chọn)

class Person:
    def __init__(self, name: str):
        self.name = name

class Student(Person):
    def __init__(self, name: str, student_id: str, grade: str):
        super().__init__(name)
        self.id = student_id
        self.grade = grade

    def __repr__(self):
        return f"Student(id='{self.id}', name='{self.name}', grade='{self.grade}')"

class StudentManager:
    def __init__(self):
        self._by_id: dict[str, Student] = {}

    # CREATE
    def add(self, student: Student) -> None:
        if student.id in self._by_id:
            raise ValueError("duplicate student id")
        self._by_id[student.id] = student

    # READ (one)
    def get(self, student_id: str) -> Student | None:
        return self._by_id.get(student_id)

    # UPDATE
    def update(self, student_id: str, *, name: str | None = None, grade: str | None = None) -> None:
        st = self._by_id.get(student_id)
        if not st:
            raise ValueError("student not found")
        if name is not None:
            st.name = name
        if grade is not None:
            st.grade = grade

    # DELETE
    def remove(self, student_id: str) -> None:
        if student_id not in self._by_id:
            raise ValueError("student not found")
        del self._by_id[student_id]

    # LIST (đổi tên để không đụng builtin `list`)
    def list_all(self) -> list[Student]:
        return list(self._by_id.values())

    # SEARCH
    def search(self, *, student_id: str | None = None, name: str | None = None, grade: str | None = None) -> list[Student]:
        results = list(self._by_id.values())
        if student_id is not None:
            results = [s for s in results if s.id == student_id]
        if name is not None:
            key = name.lower()
            results = [s for s in results if key in s.name.lower()]
        if grade is not None:
            results = [s for s in results if s.grade == grade]
        return results

if __name__ == "__main__":
    mgr = StudentManager()
    mgr.add(Student("Nguyen An", "S001", "A"))
    mgr.add(Student("Tran Binh", "S002", "B"))

    print(mgr.get("S001"))
    mgr.update("S002", grade="A")
    print(mgr.search(name="nguyen"))
    print(mgr.search(grade="A"))
    mgr.remove("S002")
    print(mgr.list_all())
