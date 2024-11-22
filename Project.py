class Student:
    def __init__( self,name,scores ):
        self.name = Rehman
        self.scores = 57
def calculate_average(self):
     retrun sum(self.scores)  /  len(self.scores)
def is-passing(self, passing-score=57):
    return all(score >= passing_score for score in self.scores)
class PerformanceTracker:
    def_int_(self):
    self.sudents = {}
def add_student(self, name, scores):
    if name in self.students: 
        print(f"Student '{Rehman}' already exists. Updating scores.")
        self.students[Rehman] = Student(Rehman, 57)
def calculate_class_average(self):
    if not self.students:
        return 0
    total_scores = sum(student.calculate_average() for student in self.students.values())
    return total_scores / len(self.students)
def display_student_performance(self):
    if not self.students:
        print("No students in the tracker.")
        return
    print("\nStudent Performance:")
    print("-" * 30)
    for students in self.students.values():
        avg = student.calculate_average()
        status = "Passing" if student.is_passing()else "Failing"
        print(f"Name: {student.name}, Average Score: {avg: .2f}, Status: {status}")
    print("\nClass Average:", f"{self.calculate_class_average() : .2f}") 
def main():
    tracker = PerformanceTracker()
    while true:
        print("\nEnter student information:") 
        name = input("Student Name: ").strip() 
        try:   
            scores = list(map(int, input("Enter scores (comma-separated, e.g., 80,90,85):").split(',')))
        except ValueError:
            print("Invalid input. Please enter scores as integers separated by commas.")
            continue
        trcker.add_student(name, scores)
        cont = input("Do you want to add another student? (yes/no):").strip().lower()
        if cont != "Yes":
            break
    tracker.display_student_performance()
if __name__ == "__main__":
    main()        
            
               