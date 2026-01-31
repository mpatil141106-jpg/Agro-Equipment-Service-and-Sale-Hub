const nav=document.querySelector(".navbar")
fetch('/headerAndFooter.html')
.then(res=>res.text())
.then(data=>{
    nav.innerHTML=data
})

const ft=document.querySelector(".feet")
fetch('/footer.html')
.then(res1=>res1.text())
.then(data1=>{
    ft.innerHTML=data1
})