console.log('hello world')
const wrksdata=document.getElementById('type')
$.ajax({
    type:'GET',
    url:'/work_type_json',
    success: function(response)
    {
        console.log(response.data)
        const workData=response.data
        workData.map(item=>{
            const option=document.createElement('type')
            option.textContent=item.name
            option.setAttribute('class','item')
            option.setAttribute('data-value',item.name)
            worksData.appendChild(option)
        }
        )
    },
    error: function(response)
    {
        console.log(error)
    }
})