from abc import ABC, abstractmethod
from typing import List, Iterator

class Person(ABC):
    """Base class for university members"""
    
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        
    @abstractmethod
    def role(self) -> str:
        """Return person's role"""
        pass


class Course:
    """Represents a university course"""
    
    def __init__(self, code: str, title: str):
        self.code = code
        self.title = title
        self._enrollments = []
        
    def add_enrollment(self, enrollment) -> None:
        """Add student enrollment"""
        self._enrollments.append(enrollment)
        
    def __iter__(self) -> Iterator['Enrollment']:
        """Iterate through enrollments"""
        return iter(self._enrollments)
        
    def __add__(self, other: 'Course') -> 'CourseGroup':
        """Combine courses using + operator"""
        return CourseGroup([self, other])


class Enrollment:
    """Tracks student-course relationships"""
    
    def __init__(self, student, course):
        self.student = student
        self.course = course


class Student(Person):
    """Student implementation"""
    
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self._courses = []
        
    def enroll(self, course: Course) -> None:
        """Enroll in a course"""
        enrollment = Enrollment(self, course)
        self._courses.append(enrollment)
        course.add_enrollment(enrollment)
        
    def __iter__(self) -> Iterator[Enrollment]:
        """Iterate through student's courses"""
        return iter(self._courses)
        
    def role(self) -> str:
        return "Student"


class Instructor(Person):
    """Instructor implementation"""
    
    def __init__(self, id: int, name: str, department: str):
        super().__init__(id, name)
        self.department = department
        
    def role(self) -> str:
        return "Instructor"


class TeachingAssistant(Student, Instructor):
    """TA implementation (multiple inheritance)"""
    
    def __init__(self, id: int, name: str, department: str):
        # Initialize both parent classes
        Student.__init__(self, id, name)
        Instructor.__init__(self, id, name, department)
        
    def role(self) -> str:
        return "Teaching Assistant"


class CourseGroup:
    """Represents a group of courses (for operator overloading)"""
    
    def __init__(self, courses: List[Course]):
        self.courses = courses
        
    def total_enrollments(self) -> int:
        return sum(len(list(course)) for course in self.courses)


# Positive Attribute Descriptor
class PositiveAttribute:
    """Descriptor for positive-valued attributes"""
    
    def __set_name__(self, owner, name):
        self.name = name
        
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
        
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        instance.__dict__[self.name] = value


# Factory method implementation
class CourseFactory:
    """Creates different types of courses"""
    
    @staticmethod
    def create_course(course_type: str, *args) -> Course:
        if course_type == "lecture":
            return Course(*args)
        elif course_type == "lab":
            return Course(*args)
        else:
            raise ValueError(f"Unknown course type: {course_type}")
