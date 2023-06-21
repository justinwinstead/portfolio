from django.db import models

class Education(models.Model):
    '''
    stores the data for educational history

      attributes:
        Degrees (TextChoices): an enumeration class to ensure data integrity/consistency of credential field
        institution (CharField): the name of the educational institution attended
        credential (CharField): indicates the degree type received
        major (CharField): the educational focus of the degree
        gpa (DecimalField): the grade point average attained in my tenure at the institution
        coursework (TextField): some of the courses taken at the institution
    '''
    Degrees = models.TextChoices("Degrees", "Associate Bachelor\'s Master\'s PhD")
    institution = models.CharField(max_length=25)
    credential = models.CharField(max_length=10, choices=Degrees.choices)
    major = models.CharField(max_length=15)
    gpa = models.DecimalField(max_digits=4, decimal_places=3)
    coursework = models.TextField(max_length=200)

    def __str__(self):
        return "{self.credential} in {self.major}"

class Skill(models.Model):
    '''
    stores the data for professional skills attained

      attributes:
        Expertises (TextChoices): an enumeration class to ensure data integrity/consistency of proficiency field
        description (CharField): a brief overview of the Skill
        proficiency (CharField): level of familiarity with the Skill
        duration (IntegerField): length of time (in years) utilizing the Skill
    '''
    Expertises = models.TextChoices("Expertises", "Basic Intermediate Advanced Master")
    description = models.CharField(max_length=30)
    proficiency = models.CharField(max_length=15, choices=Expertises.choices)
    duration = models.IntegerField()

    def __str__(self):
        return self.description
    
class Tool(models.Model):
    '''
    stores the data for computer science tools i've used

      attributes:
        Expertises (TextChoices): an enumeration class to ensure data integrity/consistency of proficiency field
        Categories (TextChoices): an enumeration class to ensure data integrity/consistency of category field
        name (CharField): the name of the Tool
        category (CharField): the field of computer science the Tool is associated with
        proficiency (CharField): level of familiarity with the Tool
        duration (IntegerField): length of time (in years) utilizing the Tool
    '''
    Expertises = models.TextChoices("Expertises", "Basic Intermediate Advanced Master")
    Categories = models.TextChoices("Categories", "Platforms Databases Frameworks Languages Programs")
    name = models.CharField(max_length=25)
    proficiency = models.CharField(max_length=15, choices=Expertises.choices)
    category = models.CharField(max_length=15, choices=Categories.choices)
    duration = models.IntegerField()

    def __str__(self):
        return self.name

class Project(models.Model):
    '''
    stores the data for computer science projects i have completed

      attributes:
        name (CharField): the name of the Project
        description (CharField): a brief overview of the Project
        languages (CharField): the names of the languages and/or frameworks used
        url (URLField): a link to the Project on GitHub
    '''
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=125)
    languages = models.CharField(max_length=30)
    url = models.URLField(max_length=75)

    def __str__(self):
        return self.name
    
class WorkHistory(models.Model):
    '''
    stores the data for previous employment positions

      attributes:
        title (CharField): the employer's title for the position
        employer (CharField): the name of the employer
        location (CharField): the city, state, and country the position was located in
        start_date (DateField): the month and year the position was started
        end_date (DateField): the month and year the position was started
        responsibilities (TextField): a description of the tasks performed in the position
    '''
    title = models.CharField(max_length=30)
    employer = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    responsibilities = models.TextField()

    def __str__(self):
      return "{self.title} at {self.employer}"
