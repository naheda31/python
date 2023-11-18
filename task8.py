class Career_portal:
    def __init__(self):
        while True:
            print(''' Welcome to Marolix technology
                                                * Admin login press 1
                                                * JobSeeker login press 2
        ''')
            n = input()
            if n == '1':
                a = Career_portal.Admin()
            elif n == '2':
                u = Career_portal.JobSeeker()
            else:
                print("Invalid option")
                s = input('press any key to continue')

    class Admin:
        job_list = []
        emp_details = []

        def __init__(self):
            print(''' Welcome to Admin portal
                                                                1.Add Jobpost
                                                                2.No of applicants
                        To add job press 1, To get Total no of applicants press 2''')
            n = input()
            if n == '1':
                self.add()
            elif n == '2':
                self.total()
            else:
                print('Jobs not found')
                s = input('press any key to continue')

        code = 1

        def add(self):
            job = {}
            job['Job-id'] = str(Career_portal.Admin.code)
            job['Role'] = input('Enter Designation of job: ')
            job['Domain'] = input('Enter domain for that designation: ')
            job['location'] = input('Enter location for that job: ')
            job['Experience'] = input('Enter experience for that role: ')
            job['CTC'] = input('Enter CTC for that role: ')
            Career_portal.Admin.job_list.append(job)
            Career_portal.Admin.code += 1
            print('Job post added succesfully')
            s = input('press any key to continue')

        def total(self):
            for d in Career_portal.Admin.emp_details:
                print(d)
            else:
                s = input('press any key to continue')

    class JobSeeker(Admin):
        def __init__(self):
            for s in Career_portal.Admin.job_list:
                print(s)
            n = input('Enter Job-id to apply, orelse press 0 to exit: ')
            if n == '0':
                print("invalid job-id")
                p = input('press any key to continue')
            else:
                for s in Career_portal.Admin.job_list:
                    if n == s.get('Job-id'):
                        d = {}
                        d['User-name'] = input('Enter your name: ')
                        d['mobile'] = input('enter mobile number: ')
                        d['age'] = input('Enter your age: ')
                        d['Job-id'] = n
                        d['Role'] = s.get('Role')
                        Career_portal.Admin.emp_details.append(d)
                        print(f"You have succesfully applied for the role of {s.get('Role')}")
                        s = input('press any key to continue')
                        break
                else:
                    print("Invalid entry")
                    s = input('press any key to continue')


c = Career_portal()