
function scroll(){
  var $tickerWrapper = $(".tickerwrapper");
  var $list = $tickerWrapper.find("ul.list");
  var $clonedList = $list.clone();
  var listWidth = 10;
  
  $list.find("li").each(function (i) {
        listWidth += $(this, i).outerWidth(true);
  });
  
  var endPos = $tickerWrapper.width() - listWidth;
  
  $list.add($clonedList).css({
    "width" : listWidth + "px"
  });
  
  $clonedList.addClass("cloned").appendTo($tickerWrapper);
  
  //TimelineMax
  var infinite = new TimelineMax({repeat: -1, paused: true});
  var time = 40;
  
  infinite
    .fromTo($list, time, {rotation:0.01,x:0}, {force3D:true, x: -listWidth, ease: Linear.easeNone}, 0)
    .fromTo($clonedList, time, {rotation:0.01, x:listWidth}, {force3D:true, x:0, ease: Linear.easeNone}, 0)
    .set($list, {force3D:true, rotation:0.01, x: listWidth})
    .to($clonedList, time, {force3D:true, rotation:0.01, x: -listWidth, ease: Linear.easeNone}, time)
    .to($list, time, {force3D:true, rotation:0.01, x: 0, ease: Linear.easeNone}, time)
    .progress(1).progress(0)
    .play();
  
  //Pause/Play		
  $tickerWrapper.on("mouseenter", function(){
    infinite.pause();
  }).on("mouseleave", function(){
    infinite.play();
  });
  }
  scroll()


function swiperFunction(){
    var swiper = new Swiper(".mySwiper", {
      slidesPreview:1,
        spaceBetween:1,
        centeredSlides: true,
        loop:true,
        speed:7000,
        autoplay: {
        delay: 2000,
        disableOnInteraction: false,
        },
      pagination: {
        el: ".swiper-pagination",
        dynamicBullets: true,
        
      },
    });}
    swiperFunction()



    

    Imgview=()=>{

      acceptfiles=document.querySelectorAll('.accept_files')
      imigi=document.querySelectorAll('.imigi')
      acceptfiles.forEach((e,i) => {
          e.addEventListener('change',()=>{
              
              imigi[i].src=URL.createObjectURL(acceptfiles[i].files[0])
          })
          
      });
  }
  Imgview()
  
  setTimeout(function() {
    $('#mydiv').fadeOut('fast');
}, 1000);


function myFunction() {
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}




function toggglePassword(){
  const togglePassword = document
  .querySelector('#togglePassword');
const password = document.querySelector('#password');


togglePassword.addEventListener('click', () => {
  // Toggle the type attribute using
  // getAttribure() method
  const type = password
      .getAttribute('type') === 'password' ?
      'text' : 'password';
      
  password.setAttribute('type', type);
  // Toggle the eye and bi-eye icon
  this.classList.toggle('bi-eye');
});
}
toggglePassword()


function toggglePassword1(){
  const togglePassword = document
  .querySelector('#togglePassword1');
const password = document.querySelector('#password1');
togglePassword.addEventListener('click', () => {
  // Toggle the type attribute using
  // getAttribure() method
  const type = password
      .getAttribute('type') === 'password' ?
      'text' : 'password';
      
  password.setAttribute('type', type);
  // Toggle the eye and bi-eye icon
  this.classList.toggle('bi-eye');
});
}
toggglePassword1()
function toggglePassword2(){
  const togglePassword = document
  .querySelector('#togglePassword2');
const password = document.querySelector('#password2');


togglePassword.addEventListener('click', () => {
  // Toggle the type attribute using
  // getAttribure() method
  const type = password
      .getAttribute('type') === 'password' ?
      'text' : 'password';
      
  password.setAttribute('type', type);
  // Toggle the eye and bi-eye icon
  this.classList.toggle('bi-eye');
});
}
toggglePassword2()

$(document).ready(function () {
  resetForms();
});

function resetForms() {
  document.forms.reset();
}