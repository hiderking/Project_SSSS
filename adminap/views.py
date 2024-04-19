from django.shortcuts import render,redirect
import datetime
# Create your views here.

from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm
# from schoolap.views import updater_data
from schoolap.models import ViewerContacts
from adminap.models import *
from adminap.forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import exceptions
import os
# Create your views here.


# *****admin panels*****

# admin dashboard

@login_required(login_url='/Admin/')
def AdminPanelHome(request):
#  admin=Admin.objects.filter(username=username)
 data={
    "updater":request.user.username,
    'category':request.user.category,
 }
 return render(request,'AdminpanelHome.html',data)

# admin swiper 
@login_required(login_url='/Admin/')
def AdminPanelHomeSwiperView(request):
       form=HomeSwiper.objects.all().order_by('position')
       data={
         'updater':request.user.username,
         'form':form,
         'category':request.user.category,
         }
       return render(request,'AdminPanelHomeSwiperView.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelHomeSwiperAdd(request):
   if(request.method=='POST'):
       form=HomeSwiperForm(request.POST,request.FILES) 
       title=request.POST.get('edit_swiper_title')
       position=request.POST.get('edit_swiper_position')
       desc=request.POST.get('edit_swiper_description')
       i=request.FILES.get('edit_swiper_image') 
       Costum=CostumUser.objects.get(username=request.user.username)
       
       home=HomeSwiper(
          title=title,
          desc=desc,
          position=int(position),
          img=i,
          uploadby=Costum,
          
          )
       home.save()
       return redirect('AdminPanelHomeSwiperView')
   
   arr=[1,2,3,4,5,6,7,8,9]
   positionfull=HomeSwiper.objects.values_list('position',flat=True)

   data={
          'updater':request.user.username,
          'arr':arr,
         'occupied':positionfull,
          }
   return render(request,'AdminPanelHomeSwiper.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelHomeSwiperEdit(request,id):
   if(request.method=='POST'):
       form=HomeSwiperForm(request.POST,request.FILES) 
       title=request.POST.get('edit_swiper_title')
       position=request.POST.get('edit_swiper_position')
       desc=request.POST.get('edit_swiper_description')
       i=request.FILES.get('edit_swiper_image') 
       postimg=HomeSwiper.objects.get(id=id).img
       if type(i)==None:
          i=i
       else:
          i=postimg
       home=HomeSwiper(
          id=id,
          title=title,
          desc=desc,
          position=int(position),
          img=i,
          uploadby=CostumUser.objects.get(username=request.user.username),
          updateDate=datetime.datetime.now()    )
       home.save()
       
       return redirect('AdminPanelHomeSwiperView')
   arr=[1,2,3,4,5,6,7,8,9]
   form=HomeSwiper.objects.get(id=id)
   positionfull=HomeSwiper.objects.values_list('position',flat=True)
   data={
          'updater':request.user.username,
          'arr':arr,
          'form':form,
          'occupied':positionfull
          }
   return render(request,'AdminPanelHomeSwiper.html',data) 

@login_required(login_url='/Admin/')
def deleteswiper(request,pk):
   form=HomeSwiper.objects.get(id=pk)
   form.delete()
   messages.info(request,"Delete successfully")
   return redirect('AdminPanelHomeSwiperView')




# school achievement
@login_required(login_url='/Admin/')
def AdminPanelAchievementView(request):
   form=Achievement.objects.all().order_by('updateDate')
   data={
      "form":form,
      "updater":request.user.username,
      'category':request.user.category,
   }
   return render(request,
   'AdminPanelAchievementView.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelAchievementAdd(request):
    if(request.method=='POST'):
      form=AchievementForm(request.POST)
      experience_year=request.POST.get('experience_year')
      teacher_no=request.POST.get('teacher_no')
      bright_students=request.POST.get('bright_students')
      glorious_alumini=request.POST.get('glorious_alumini')
      uploadby=CostumUser.objects.get(username=request.user.username)
      form=Achievement(
          year_of_experiences=experience_year,
          teacher_no=teacher_no,
          bright_students=bright_students,
          glorious_alumini=glorious_alumini,
          uploadby=uploadby
       )
      form.save()
      messages.info(request,"Successfully Added")
      return redirect('AdminPanelAchievementView')
    data={
       "updater":request.user.username
       
    }
    return render(request,"AdminPanelAchievement.html",data)

@login_required(login_url='/Admin/')
def AdminPanelAchievementEdit(request,pk):
    form=Achievement.objects.get(id=pk)
    frm=form
    if(request.method=='POST'):
         experience_year=request.POST.get('experience_year')
         teacher_no=request.POST.get('teacher_no')
         bright_students=request.POST.get('bright_students')
         glorious_alumini=request.POST.get('glorious_alumini')
         form=Achievement(
            id=pk,
            year_of_experiences=experience_year,
            teacher_no=teacher_no,
            bright_students=bright_students,
            glorious_alumini=glorious_alumini,
            uploadby=CostumUser.objects.get(username=request.user.username),
            updateDate=datetime.datetime.now()

         )
         form.save()
         return redirect('AdminPanelAchievementView')
    data={
       "form":frm,
       "updater":request.user.username
    }
    return render(request,"AdminPanelAchievement.html",data)



# admin panel about
@login_required(login_url='/Admin/')
def AdminPanelAboutView(request):
   vision=AboutVision.objects.all().order_by('updateDate')[:1]
   principle=AboutPrinciple.objects.all().order_by('updateDate')[:1]
   history=AboutHistory.objects.all().order_by('updateDate')[:1]
   data={
      'vision':vision,
      'principle':principle,
      'history':history,
      'updater':request.user.username,
      'category':request.user.category,
   
   }

   return render (request,'AdminPanelAboutView.html',data)


@login_required(login_url='/Admin/')
def AdminPanelAboutVision(request,vision_id):
   if request.method=='POST':
      fp=request.POST.get('vision-mission-para1')
      sp=request.POST.get('vision-mission-para2')
      tp=request.POST.get('vision-mission-para3')
      fop=request.POST.get('vision-mission-para4')
      about=AboutVision(
         auto_increment_id=int(vision_id),
         firstpara=fp,
         secondpara=sp,
         thirdpara=tp,
         fourthpara=fop,
         uploadby=CostumUser.objects.get(username=request.user.username),
         updateDate=datetime.datetime.now()  )
      about.save()
      messages.success(request,'Successfully Edit')
      return redirect('AdminPanelAboutView')
   form=AboutVision.objects.get(auto_increment_id=vision_id)
   data={
   'updater':request.user.username,
    "form":form
    }
   
   return render(request,'AdminPanelAboutVision.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelAboutVisionAdd(request):
   if request.method=='POST':
      fp=request.POST.get('vision-mission-para1')
      sp=request.POST.get('vision-mission-para2')
      tp=request.POST.get('vision-mission-para3')
      fop=request.POST.get('vision-mission-para4')
      about=AboutVision(
         firstpara=fp,
         secondpara=sp,
         thirdpara=tp,
         fourthpara=fop,
         uploadby=CostumUser.objects.get(username=request.user.username), )
      
      about.save()
      messages.success(request,'Successfully add')
      return redirect('AdminPanelAboutView')
   data={
      'updater':request.user.username
   }
   return render(request,'AdminPanelAboutVision.html',data) 


@login_required(login_url='/Admin/')
def AdminPanelAboutPrinciple(request,p_id):
   about=AboutPrinciple(auto_increment_id=p_id)
   postimg=about.img
   if(request.method=='POST'):
      
      if len(request.FILES) !=0:
         if len(str(about.img))>0:
            os.remove(about.img.path)
         img=request.FILES['principle-img']
         if type(img)==None:
            about.img=postimg
         else:
            about.img=img
         about.title=request.POST.get('principle-name')
         about.principleintro=request.POST.get('Short-Desc')
         about.firstpara=request.POST.get('principle-para1')
         about.secondpara=request.POST.get('principle-para2')
         about.thirdpara=request.POST.get('principle-para3')
         about.fourthpara=request.POST.get('principle-para4')
         about.uploadby=CostumUser.objects.get(username=request.user.username)
         about.updateDate=datetime.datetime.now()
         about.save()
         messages.success(request,'Successfully Update')
         return redirect('AdminPanelAboutView')
   form=AboutPrinciple.objects.get(auto_increment_id=p_id)
   data={
      'updater':request.user.username,
      "form":form
      }
   return render(request,'AdminPanelAboutPrinciple.html',data)

@login_required(login_url='/Admin/')
def AdminPanelAboutPrincipleAdd(request):
   about=AboutPrincipleForm(request.POST,request.FILES)
   if(request.method=='POST'):
         about=AboutPrinciple()
         about.img=request.FILES['principle-img']
         about.title=request.POST.get('principle-name')
         about.principleintro=request.POST.get('Short-Desc')
         about.firstpara=request.POST.get('principle-para1')
         about.secondpara=request.POST.get('principle-para2')
         about.thirdpara=request.POST.get('principle-para3')
         about.fourthpara=request.POST.get('principle-para4')
         about.uploadby=CostumUser.objects.get(username=request.user.username)
         about.save()
         messages.success(request,'Successfully Update')
         return redirect('AdminPanelAboutView')
   data={
      'updater':request.user.username
   }
   return render(request,'AdminPanelAboutPrinciple.html',data)


@login_required(login_url='/Admin/')
def AdminPanelAboutHistory(request,history_id):
   if(request.method=='POST'):
      form=AboutHistoryForm(request.POST)
      fp=request.POST.get('History-para1')
      sp=request.POST.get('History-para2')
      tp=request.POST.get('History-para3')
      fop=request.POST.get('History-para4')
      about=AboutHistory(
         auto_increment_id=history_id,
         firstpara=fp,
         secondpara=sp,
         thirdpara=tp,
         fourthpara=fop,
         uploadby=CostumUser.objects.get(username=request.user.username),
         updateDate=datetime.datetime.now()
         )
      messages.success(request,'Successfully Edit')
      about.save()
      return redirect('AdminPanelAboutView')
   form=AboutHistory.objects.get(auto_increment_id=history_id)
   data={
      "form":form,
      'updater':request.user.username
   }
   return render(request,'AdminPanelAboutHistory.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelAboutHistoryAdd(request):
   if(request.method=='POST'):
      form=AboutHistoryForm(request.POST)
      fp=request.POST.get('History-para1')
      sp=request.POST.get('History-para2')
      tp=request.POST.get('History-para3')
      fop=request.POST.get('History-para4')
      about=AboutHistory(
         firstpara=fp,
         secondpara=sp,
         thirdpara=tp,
         fourthpara=fop,
         uploadby=CostumUser.objects.get(username=request.user.username),
         )
      about.save()
      messages.success(request,'Successfully Add')
      return redirect('AdminPanelAboutView')
   data={
      'updater':request.user.username
   }
   return render(request,'AdminPanelAboutHistory.html',data) 


# introduction
@login_required(login_url='/Admin/')
def AdminPanelIntroductionView(request):
      Intro=Introduction.objects.all().order_by('updateDate')[:1]
      data={
      'Intro':Intro,
      "updater":request.user.username,
      'category':request.user.category,

        }
      return render(request,"AdminPanelIntroductionView.html",data)

@login_required(login_url='/Admin/')
def AdminPanelIntroductionEdit(request,id):
   if(request.method=='POST'):
      form=IntroductionForm(request.POST)
      fp=request.POST.get('Introduction-para1')
      sp=request.POST.get('Introduction-para2')
      tp=request.POST.get('Introduction-para3')
      Intro=Introduction(
         id=id,
         firstpara=fp,
         secondpara=sp,
         thirdpara=tp,
         uploadby=CostumUser.objects.get(username=request.user.username),
         updateDate=datetime.datetime.now()
         )
      Intro.save()
      return redirect('AdminPanelIntroductionView')
   form=Introduction.objects.get(id=id)
   data={
      "form":form,
      "updater":request.user.username
   }
   return render(request,'AdminPanelIntroduction.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelIntroductionAdd(request):
   if(request.method=='POST'):
      form=IntroductionForm(request.POST)
      fp=request.POST.get('Introduction-para1')
      sp=request.POST.get('Introduction-para2')
      tp=request.POST.get('Introduction-para3')
      Intro=Introduction(
         firstpara=fp,
         secondpara=sp,
         thirdpara=tp,
         uploadby=CostumUser.objects.get(username=request.user.username),
         )
      Intro.save()
      return redirect('AdminPanelIntroductionView')

   data={
      "updater":request.user.username
   }
   return render(request,'AdminPanelIntroduction.html',data) 




# admin panel admisiion
# @login_required(login_url='/Admin/')
# def AdminPanelAdmission(request):
#    return render(request,'AdminPanelAdmission.html',{'updater':request.user.username}) 



# admin panel notice
@login_required(login_url='/Admin/')
def AdminPanelNoticeAdd(request):
   if(request.method=='POST'):
      form=NoticeForm(request.POST,request.FILES)
      title=request.POST.get('notice_files_title')
      desc=request.POST.get('notice_files_description')
      img=request.FILES.get('notice_img')
      title2=request.POST.get('notice_file_title1')
      file2=request.FILES.get('notice_file1')
      title3=request.POST.get('notice_file_title2')
      file3=request.FILES.get('notice_file2')
      form=Notice(
          title=title,
          description=desc,
          file1=img,
          title2=title2,
          file2=file2,
          title3=title3,
          file3=file3,
          uploadby=CostumUser.objects.get(username=request.user.username),
       )
      form.save()
      messages.info(request,"Successfully vayo")
      return redirect('AdminPanelNoticeView')
   data={'updater':request.user.username}
   return render(request,'AdminPanelNotice.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelNoticeView(request):
   form=Notice.objects.all().order_by('updateDate')
   data={
      'updater':request.user.username,
      "form":form,
      'category':request.user.category,

      }
   return render(request,'AdminPanelNoticeView.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelNoticeEdit(request,pk):
   form=Notice.objects.get(id=pk)
   frm=form
   if(request.method=='POST'):
      form=NoticeForm(request.POST,request.FILES)
      form=Notice()

      form.title=request.POST.get('notice_files_title')
      form.description=request.POST.get('notice_files_description')
      form.file1=request.FILES.get('notice_img')
      form.title2=request.POST.get('notice_file_title1')
      form.file2=request.FILES.get('notice_file1')
      form.title3=request.POST.get('notice_file_title2')
      form.file3=request.FILES.get('notice_file2')
      form.uploadby=CostumUser.objects.get(username=request.user.username)
      form.updateDate=datetime.datetime.now()
      form.save()
      return redirect("AdminPanelNoticeView")

   data={
      'updater':request.user.username,
         "form":frm
         }
   return render(request,'AdminPanelNotice.html',data) 

@login_required(login_url='/Admin/')
def deletenotice(request,pk):
   form=Notice.objects.get(id=pk)
   form.delete()
   messages.info(request,"Delete successfully")
   return redirect('AdminPanelNoticeView')




#  adminpanel samachar 
@login_required(login_url='/Admin/')
def AdminPanelNewsAdd(request):
   if(request.method=='POST'):
      form=NewsForm(request.POST)
      title=request.POST.get('samachar_title')
      link=request.POST.get('samachar_url')
      form=News(
          title=title,
          link=link,
          uploadby=CostumUser.objects.get(username=request.user.username),
       )
      form.save()
      messages.info(request,"Successfully vayo")
      return redirect('AdminPanelNewsView')
   data={
      'updater':request.user.username
      }
   return render(request,'AdminPanelNews.html',data)

@login_required(login_url='/Admin/')
def AdminPanelNewsView(request):
   form=News.objects.all().order_by('updateDate')
   data={
      'category':request.user.category,
      'updater':request.user.username,"form":form,}
   return render(request,'AdminPanelNewsView.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelNewsEdit(request,pk):
    form=News.objects.get(id=pk)
    frm=form
    if(request.method=='POST'):
         form.id=pk
         form.title=request.POST.get('samachar_title')
         form.link=request.POST.get('samachar_url')
         form.uploadby=CostumUser.objects.get(username=request.user.username),
      
         form.updateDate=datetime.datetime.now()
         form.save()
         return redirect('AdminPanelNewsView')
    data={
       'updater':request.user.username,
       "form":frm
       }
    return render(request,'AdminPanelNews.html',data) 

@login_required(login_url='/Admin/')
def deletenews(request,pk):
   form=News.objects.get(id=pk)
   form.delete()
   messages.info(request,"Delete successfully")
   return redirect('AdminPanelNewsView')
  

# admin panel gallery
@login_required(login_url='/Admin/')
def AdminPanelGalleryView(request):
   form= Gallery.objects.all().order_by('updateDate')
   data={
      'category':request.user.category,
      'updater':request.user.username,"form":form
      }
   return render(request,'AdminPanelGalleryView.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelGalleryAdd(request):
    form=GalleryForm(request.POST,request.FILES)
    if(request.method =='POST'):
      form=Gallery()
      title=request.POST.get('gallery_img_title')
      img=request.FILES.get('gallery_img')
      
      form.title=title
      form.img=img
      form.uploadby=CostumUser.objects.get(username=request.user.username)
      form.save()
      messages.info(request,"Successfully vayo")
      return redirect('AdminPanelGalleryView')
    

    data={
       'updater':request.user.username
       }
    return render(request,'AdminPanelGallery.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelGalleryEdit(request,pk):
   form=Gallery.objects.get(id=pk)
   frm=form
   if(request.method=='POST'):
      if len(request.FILES) !=0:
         if len(str(form.img)) >0:
            os.remove(form.img.path)
         form.id=pk
         form.title=request.POST.get('gallery_img_title')
         form.img=request.FILES.get('gallery_img')
         form.uploadby=CostumUser.objects.get(username=request.user.username),
         form.updateDate=datetime.datetime.now()
         form.save()
         return redirect('AdminPanelGalleryView')
   
   data={
      'updater':request.user.username,
         "form":frm
         }
   return render(request,'AdminPanelGallery.html',data) 

@login_required(login_url='/Admin/')
def deletegallery(request,pk):
   form=Gallery.objects.get(id=pk)
   form.delete()
   messages.info(request,"Delete successfully")
   return redirect('AdminPanelGalleryView')



# admin panel more
@login_required(login_url='/Admin/')
def AdminPanelMoreAdd(request):
   if(request.method=='POST'):
      form=MoreForm(request.POST,request.FILES)
      title=request.POST.get('file_title')
      file=request.FILES.get('filename')
      form=MoreDoc(
          title=title,
          file=file,
          uploadby=CostumUser.objects.get(username=request.user.username),
       )
      form.save()
      messages.info(request,"Successfully vayo")
      return redirect('AdminPanelMoreView')
   data={
      'updater':request.user.username
      }
   return render(request,'AdminPanelMore.html',data)

@login_required(login_url='/Admin/')
def AdminPanelMoreView(request):
   form=MoreDoc.objects.all().order_by('updateDate')
      
   data={
      'category':request.user.category,
      'updater':request.user.username,
      "form":form}
   return render(request,'AdminPanelMoreView.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelMoreEdit(request,pk):
    form=MoreDoc.objects.get(id=pk)
    frm=form
    postfile=form.file
    if(request.method=='POST'):
      if len(request.FILES) !=0:
         if len(str(form.img)) >0:
            os.remove(form.img.path)
         form.id=pk
         form.title=request.POST.get('file_title')

         file=request.FILES.get('filename')
         if type(file)==None:
            form.file=postfile
         else:
            form.file=file
         form.uploadby=CostumUser.objects.get(username=request.user.username),
      
         form.updateDate=datetime.datetime.now()
         form.save()
         return redirect('AdminPanelMoreView')
    data={
       'updater':request.user.username,
       "form":frm
       }
    return render(request,'AdminPanelMore.html',data) 

@login_required(login_url='/Admin/')
def deletemore(request,pk):
   form=MoreDoc.objects.get(id=pk)
   form.delete()
   messages.info(request,"Delete successfully")
   return redirect('AdminPanelMoreView')



# admin panel contact
@login_required(login_url='/Admin/')
def AdminPanelContactLinkView(request):
   contact=Contact.objects.all().order_by('updateDate')[:1]
   social=Social.objects.all().order_by('updateDate')[:1]
   data={
      'contact':contact,
      'social':social,
      'updater':request.user.username,
      'category':request.user.category,

      }
   return render (request,'AdminPanelContactLinkView.html',data)


@login_required(login_url='/Admin/')
def AdminPanelContactAdd(request):
   if request.method=='POST':
      contact=Contact(
         location=request.POST.get('location_link'),
         gmail_api=request.POST.get('gmail_api'),
         gmail=request.POST.get('gmail_link'),
         phn_no=request.POST.get('phn_no'),uploadby=CostumUser.objects.get(username=request.user.username),
           ),
         
      contact.save()
      return redirect('AdminPanelContactLinkView')
   data={
      'updater':request.user.username}
   return render(request,'AdminPanelContact.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelContactEdit(request,pk):
   if request.method=='POST':
      contact=Contact(
         id=int(pk),
         location=request.POST.get('location_link'),
         gmail_api=request.POST.get('gmail_link'),
         gmail=request.POST.get('gmail_api'),
         phn_no=request.POST.get('phn_no'),
         uploadby=CostumUser.objects.get(username=request.user.username),
         updateDate=datetime.datetime.now()  )
      contact.save()
      return redirect('AdminPanelContactLinkView')
   form=Contact.objects.get(id=pk)
   data={
      'updater':request.user.username,
      "form":form
      }
   return render(request,'AdminPanelContact.html',data)


@login_required(login_url='/Admin/')
def AdminPanelSocialAdd(request):
   if(request.method=='POST'):
      social=Social()
      social.facebook=request.POST.get('facebook_link')
      social.twitter=request.POST.get('twitter_link')
      social.linkedin=request.POST.get('linkedin_link')
      social.uploadby=CostumUser.objects.get(username=request.user.username),
      social.save()
      return redirect('AdminPanelContactLinkView')
   data={
      'updater':request.user.username
         }
   return render(request,'AdminPanelSocial.html',data)

@login_required(login_url='/Admin/')
def AdminPanelSocialEdit(request,pk):
   if(request.method=='POST'):
      social=Social()
      social.id=pk
      social.facebook=request.POST.get('facebook_link')
      social.twitter=request.POST.get('twitter_link')
      social.linkedin=request.POST.get('linkedin_link')
      social.uploadby=CostumUser.objects.get(username=request.user.username),
      social.updateDate=datetime.datetime.now()
      social.save()
      return redirect('AdminPanelContactLinkView')
   
   form=Social.objects.get(id=pk)
   
   data={
      'updater':request.user.username,
      "form":form,
      }
   return render(request,'AdminPanelSocial.html',data)


# contact form view
@login_required(login_url='/Admin/')
def AdminPanelContactsView(request):
   form=ViewerContacts.objects.all()
   return render (request,'AdminPanelContactsView.html',{'updater':request.user.username,"form":form})

# admin profile
@login_required(login_url='/Admin/')
def AdminProfile(request):
   form=Admin()
   if request.user.category == "admin":
      try:
        form=Admin.objects.get(username=request.user.username)
        
      except form.DoesNotExist:
          form = None
   elif request.user.category == "moderator":
      try:
        form=Moderator.objects.get(username=request.user.username)
      except form.DoesNotExist:
          form = None

   Mode=Moderator()
   try:
        Mode=Moderator.objects.all()
   except Mode.DoesNotExist:
          Mode = None
   user=CostumUser.objects.get(username=request.user.username)  
   data={
      "updater":request.user.username,
      "category":request.user.category,
      'form':form,
      'mode':Mode,
      'user':user
   }
   return render(request,'AdminProfile.html',data)


@login_required(login_url='/Admin/')
def AdminProfileEdit(request,pk):
   form=AdminForm(request.POST,request.FILES)
   form2=ModeratorForm(request.POST,request.FILES)
   category=request.user.category
   if(request.method=='POST'):
      if category=='admin':
         form=Admin.objects.get(username=pk)
         if len(request.FILES) !=0:
               if len(str(form.img)) >0:
                  os.remove(form.img.path)
               form.first_name=request.POST.get('first_name')
               form.middle_name=request.POST.get('middle_name')
               form.last_name=request.POST.get('last_name')
               form.post=request.POST.get('admin_post')
               form.img=request.FILES.get('gallery_img')
               form.address=request.POST.get('address')
               form.phn_no=request.POST.get('phn_no')
               form.address=request.POST.get('address')
               form.save()
               email=request.POST.get('gmail')
               CostumUser.objects.filter(username=request.user.username).update(email=email)
               messages.success(request,"Successfully updated")
               return redirect('AdminProfile')
      elif category=='moderator':
           form2=Moderator.objects.get(username=pk)
           if len(request.FILES) !=0:
               if len(str(form2.img)) >0:
                  os.remove(form2.img.path)
               form2.first_name=request.POST.get('first_name')
               form2.middle_name=request.POST.get('middle_name')
               form2.last_name=request.POST.get('last_name')
               form2.username=request.user.username
               form2.post=request.POST.get('admin_post')
               form2.img=request.FILES.get('gallery_img')
               form2.address=request.POST.get('address')
               form2.phn_no=request.POST.get('phn_no')
               form2.address=request.POST.get('address')
               form2.user=CostumUser.objects.get(username=request.user.username)
               form2.save()
               email=request.POST.get('gmail')
               CostumUser.objects.filter(username=request.user.username).update(email=email)
               messages.success(request,"Successfully updated")
               return redirect('AdminProfile')
   
   arr=['Administrator','Teacher','Principle']
   if category==request.user.username:
      form=Admin.objects.get(username=request.user.username)
   elif category==request.user.username:
      form=Moderator.objects.get(username=request.user.username)
   user=CostumUser.objects.get(username=request.user.username)
   data={
      "updater":request.user.username,
      "category":request.user.category,
      'form':form,
      'arr':arr,
      'user':user,
   }
   return render(request,'AdminProfileEdit.html',data)


@login_required(login_url='/Admin/')
def AdminProfileAdd(request):
   form=AdminForm(request.POST,request.FILES)
   if(request.method == 'POST'):
            form=Admin()
            form.username=request.user.username
            form.user=CostumUser.objects.get(username=request.user.username)
            form.first_name=request.POST.get('first_name')
            form.middle_name=request.POST.get('middle_name')
            form.last_name=request.POST.get('last_name')
            form.post=request.POST.get('admin_post')
            form.img=request.FILES.get('gallery_img')
            form.address=request.POST.get('address')
            form.phn_no=request.POST.get('phn_no')
            form.address=request.POST.get('address')
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('AdminProfile') 
   
   arr=['Administrator','Teacher','Principle']
   data={
      "updater":request.user.username,
      "category":request.user.category,
      'form':form,
      'arr':arr,
   }
   return render(request,'AdminProfileEdit.html',data)


@login_required(login_url='/Admin/')
def AdminNewModeratorAdd(request):
   form=Moderator(request.POST,request.FILES)
   user=CostumUserForm(request.POST)
   if request.method =='POST':
      user=CostumUser()
      username=request.POST.get('moderator_username')
      user.username=username
      user.category='moderator'
      user.email=request.POST.get('gmail')
      user.set_password=request.POST.get('password')
      user.save()
      form=Moderator()
      form.username=username
      form.user=CostumUser.objects.get(username=username)
      form.first_name=request.POST.get('first_name')
      form.middle_name=request.POST.get('middle_name')
      form.last_name=request.POST.get('last_name')
      form.post=request.POST.get('admin_post')
      form.img=request.FILES.get('gallery_img')
      form.address=request.POST.get('address')
      form.phn_no=request.POST.get('phn_no')
      form.address=request.POST.get('address')
      form.save()
      messages.success(request,'Successfully create new moderator')
      return redirect('AdminProfile') 
   
   arr=['Administrator','Teacher','Principle']
   data={
      "updater":request.user.username,
      "category":request.user.category,
      'form':form,
      'arr':arr,
   }
   return render(request,'AdminNewModerator.html',data)



@login_required(login_url='/Admin/')
def AdminProfilechangePassword(request):
   if request.method== "POST":
      form=PasswordChangeForm(user=request.user,data=request.POST)
      if form.is_valid():
         form.save()
         messages.success(request,"! Password change successfully...")
         return redirect("Admin")
   else:
      form=PasswordChangeForm(user=request.user)
   data={
      "updater":request.user.username,
      "category":request.user.category,
      'form':form
   }
   return render(request,'AdminProfilechangePassword.html',data)


# def AdminNewModerator(request):
#    form=CostumUser()
#    if(request.method=='POST'):
#             form=CostumUser()
#             form.username=request.POST.get('moderator_username')
#             form.password=request.POST.get('moderator_password')
#             form.category="moderator"
#             form.save()
#             messages.success(request,'Successfully created new moderator')
#             return redirect('AdminProfile')
#    data={
#       "updater":request.user.username,
#       "category":request.user.category,
#       'form':form
#    }
#    return render(request,'AdminNewModerator.html',data)
