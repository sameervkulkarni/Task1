class Sqlop:

    def __init__(self):
        pass

    def operations(self, s1, s2, s3, s4, s5):
        total = s1+s2+s3+s4+s5
        avg = (s1+s2+s3+s4+s5)/5
        if avg<35:
            grade = 'F'
        elif 35 <= avg < 60:
            grade = 'C'
        elif 60 <= avg < 75:
            grade = 'B'
        elif 75 <= avg < 90:
            grade = 'A'
        elif 90 <= avg <= 100:
            grade = 'S'
        out = [total, avg, grade]

        return out
