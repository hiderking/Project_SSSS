const ImgForSlider=[
   

{
    img:"assets/img/lab (1).jpg' ",
    title:"samjhana panday",
    para:" +2 Topper"

},
{
    img:"assets/img/lab (1).jpg' ",
    title:"shree sarbajanik secondary school",
    para:"Chhatradev-5 , Arghakhanchi , Nepal"
},

{
    img:"assets/img/prize_distrubution (4).png' ",
    title:" group photo",
    para:"grade 8"
    

},
{
    img:"assets/img/prize_distrubution (2).png' ",
    title:"sarmila panday",
    para:" 8 Topper"
    

},

{
    img:"assets/img/swagat (12).png' ",
    
    title:"swagat karyakaram",
    para:"wlcome program "

},
{
    img:"assets/img/swagat (15).png' ",
    
    title:"cultural dance",
    para:"sports week"

},
{
    img:"assets/img/swagat (8).png' ",
    title:"assets/img/swagat (1).png",
    para:"sports week"

},


{
    img:"assets/img/swagat (15).png' ",
    title:"cultural dance",
    para:"sports week"

},
{
    img:"assets/img/swagat (8).png' ",
    title:"2079 sports week moments",
    para:"sports week"

},
]


// const swiper =document.querySelector("#swiper")

// const oldArr=document.querySelectorAll(".swiper-slide")
// loldArr=oldArr.length


// function createSwiperSlide(loldArr){
//     sizeOfIFS=ImgForSlider.length
//     console.log(sizeOfIFS)
    
//     for(i=0;i<sizeOfIFS-loldArr;i++){
//         const swiperdiv=document.createElement("div");
    
//         swiperdiv.classList.add("swiper-slide")
//         swiperdiv.classList.add("position-relative")
    
    
//         swiperdiv.innerHTML=` 
//         <img class="swiperImg" src="assets/img/lab (1).jpg" alt="photo">
//           <div id="slider_slide_heading"  class="slider_slide_heading position-absolute lh-1
//           ">
//             <h6 id="swiperTitle" class="swiperTitle text-capitalize fw-bold fs-3 text-white ">Shree Sarbajanik secondary school
//             </h6> 
//             <p id="swiperPara" class="swiperPara text-capitalize fw-bold fs-6 text-white ">Arghakanchi Nepal</p>
//           </div>
//         `
//         swiper.appendChild(swiperdiv)

        

        
    
//     }
// }



// function change_photo(){
  
//     const swiperTitle=document.querySelectorAll(".swiperTitle")
//     const swiperPara=document.querySelectorAll(".swiperPara")
//     const swiperImg=document.querySelectorAll(".swiperImg")
    
    
  
//     for(i=0;i<sizeOfIFS;i++){
        
//         swiperImg[i].src= "{% static '"+ ImgForSlider[i].img+"'%}"
//         swiperTitle[i].innerHTML=ImgForSlider[i].title;
//         swiperPara[i].innerHTML=ImgForSlider[i].para;
//         console.log(ImgForSlider[i].img)
//         console.log(i)
       

// }
// }


const Notice=[
    {
        title:"holiday notice dashain tihar",
        link:"assets/img/prize_distrubution (2).png",
        date:"2023/4/5"

},

{
    title:"बस पास सम्बन्धी सूचना ०८०.०६.१६",
    link:"assets/img/library (3).jpg",
    date:"2023/5/5"

},

{
    title:"picnic program",
    link:"assets/img/PT Java Labsheet 1.pdf",
    date:"2023/8/5"

},

{
    title:"welcome program",
    link:"assets/img/library (3).jpg",
    date:"2023/10/5"

},

{
    title:"school day programming ",
    link:"assets/img/PT Java Labsheet 1.pdf",
    date:"2023/12/5"

},


]



size_Notice=Notice.length
console.log(size_Notice)


function createNoticeTr(Notice){
    const table_tr=document.querySelectorAll(".tr")
    size_tr=table_tr.length

const table=document.querySelector("#table")
    
    for(i=0;i<size_Notice-size_tr;i++){
        const tr=document.createElement("tr");
    
        tr.classList.add("tr")
    
    
        tr.innerHTML=` 
        <td>
        <div class="d-flex flex-column recent_notice_div">
        
        <a class="home-notice-title text-decoration-none text-black blue-hover fw-bold" href="assets/img/library (3).jpg">Internal Assessment Schedule, Spring 2023 ( Masters Program)</a>
      <p class="home-notice_date">2023/2/4</p>
      </div>
      </td>

      <td><a class="home-notice-download" href="assets/img/library (3).jpg" target="_blank" download><i class="bi bi-download color_blue fw-bold text"></i></a></td>
        `
    table.appendChild(tr);  
    
    }
}



function change_home_notice(){
  
   
const home_notice_title=document.querySelectorAll(".home-notice-title");
const home_notice_date=document.querySelectorAll(".home-notice_date");
const home_notice_download=document.querySelectorAll(".home-notice-download")
    
    
  
    for(i=0;i<size_Notice;i++){
        
        home_notice_title[i].innerHTML=Notice[i].title;
        home_notice_title[i].href= "{% static '"+Notice[i].link+"' %}"
        home_notice_date[i].innerHTML=Notice[i].date;
        home_notice_download[i].href="{% static '"+Notice[i].link +"' %}"
       

}
}

createNoticeTr(Notice)
change_home_notice()



// scroll notice dom manupulation 



function createScrollNotice(Notice){
    const listitem=document.querySelectorAll(".listitem")
    size_listitem=listitem.length

const list=document.querySelector(".list")
    
    for(i=0;i<size_Notice-size_listitem;i++){
        consta=document.createElement("li");
    
       a.classList.add("listitem")
    
    
       a.innerHTML=` 
       <a class="notice-scroll-a text-decoration-none text-capitalize text-opacity7 fw-bold text-black blue-hover" href="assets/other links/notices_open.html">Internal Assessment Schedule, Spring 2023 ( Masters Program)</a>
       
        `
        list.appendChild(a)

    }
}


function change_scroll_notice(){
  
   
    const notice_scroll_a=document.querySelectorAll(".notice-scroll-a");
   
        
        
      
        for(i=0;i<size_Notice;i++){
            
            notice_scroll_a[i].innerHTML=Notice[i].title;
           
           
    
    }
    }
createScrollNotice(Notice)
change_scroll_notice()
