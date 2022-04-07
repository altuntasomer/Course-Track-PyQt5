class Course:
    
    def __init__(self, course_name, course_link, progress):
        self.course_name = course_name
        self.course_link = course_link
        self.progress = progress

    def get_course_name(self):
        return self.course_name
    
    def get_course_link(self):
        return self.course_link
    
    def get_progress(self):
        return self.progress
    
