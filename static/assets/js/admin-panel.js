
var edit_title=document.getElementById("edit_swiper_title")
 var edit_position=document.getElementById("edit_swiper_position")
 var edit_description=document.getElementById("edit_swiper_description")
 var edit_image=document.getElementById("edit_swiper_image")

// console.log(edit_title,edit_position,edit_image,edit_description)

var title = document.getElementsByClassName('swiper_title')
var desc = document.getElementsByClassName('swiper_description')
var link = document.getElementsByClassName('swiper_image_link')
var position = document.querySelectorAll(".swiper_position");
const edit = document.querySelectorAll('.edit_btn');
const deleted = document.querySelectorAll('.delete_btn');
const tbody = document.getElementById("tbody");
var submit = document.getElementById("submit1");
var imgi = document.getElementById("img1");
// console.log(link)

// edit function 
function myfunction(){
    console.log(typeof(edit_image.value))
    imgi.src=URL.createObjectURL(edit_image.files[0])
}
    edit.forEach((e, i) => {

        e.addEventListener('click', () => {

            index = i
            submit.value="Edit Swiper"
            edit_title.value=title[i].value
            edit_description.value=desc[i].value
            edit_position.selectedIndex=String(position[i].value)
            console.log(String(link[i].src))
            imgi.src=link[i].src

        
        })
    })


function showImage(){
    var editer=document.getElementById('img_showing')
        imgi.src=URL.createObjectURL(editer.files[0])
    }

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
