from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,username,password=None,**extra_fields):
        if not username:
            raise ValueError("username is required")
        elif str(username) < 8:
            raise ValueError("Username must be more than 8  characters?")
        else:
            extra_fields['email']=self.normalize_email(extra_fields['email'])
            category=extra_fields['category']
            if category == 'admin':
                user=self.model(username=username,**extra_fields)
                user.set_password(password)
                user.save(using=self.db)
                return user
            else:
                raise ValueError("only user used a createsuperuser")


    def create_superuser(self,username,password=None,**extra_fields):
       extra_fields.setdefault('is_staff',True) 
       extra_fields.setdefault('is_superuser',True) 
       extra_fields.setdefault('is_active',True)

       return self.create_user(username,password,**extra_fields) 