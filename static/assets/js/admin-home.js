
var edit_title=document.getElementById("edit_image_title")
 var edit_position=document.getElementById("swiper_position")
 var edit_description=document.getElementById("edit_swiper_description")
 var edit_image=document.getElementById("swiper_image_link")

console.log(edit_title,edit_position,edit_image,edit_description)

var title = document.getElementsByClassName('swiper_title')
var desc = document.getElementsByClassName('swiper_description')
var link = document.getElementsByClassName('swiper_img_link')
var position = document.querySelectorAll(".swiper_position");

const edit = document.querySelectorAll('.edit_btn');
const deleted = document.querySelectorAll('.delete_btn');

const tbody = document.getElementById("tbody");


var submit = document.getElementById("submit1");
var submit = document.getElementById("img1");

// edit function 


    edit.forEach((e, i) => {

        e.addEventListener('click', () => {

            index = i
            edit_title.value=title.value
            edit_description.value=desc.value
            submit.value="Edit Image"
            img1.src=link.src
            
        
            
        })
    })
   