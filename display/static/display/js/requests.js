const loadBlogs = async() => {
    const response = await fetch('http://127.0.0.1:8000/api/blogs/')
    .then(response => response.json())
    .then(data => {
        for(let i = 0; i < data.length; i++) {
            document.getElementById(`category${i+1}`).innerHTML = data[i].categories[0].category_name
            document.getElementById(`image${i+1}`).setAttribute('src', data[i].image)
            document.getElementById(`blog_list${i+1}`).innerHTML += 
            `<span class='p-2 text-muted mt-auto date_time' style='font-size: 14px;'>
            ${data[i].date_posted} | ${data[i].time_to_read} min to read
            </span>` + '<br />'
            document.getElementById(`heading${i+1}`).innerHTML = data[i].title
        }
    }); 

    return response
}

const blogDetail = async(url) => {
    const response = await fetch(url)
    .then(response => response.json())
    .then(data => {
        document.getElementById("image").setAttribute('src', data.image)
        document.getElementById("content_holder").innerHTML += 
        `<h3 class='mt-5'>${data.title}</h1
        <p class='mt-2'>${data.content}</p>
        `
    });
    $(".container").attr('style', 'height:auto;')

    return response 
}

const blogCreate = (url) => {
    $(document).ready(function() {
        $('#submit_blog').click(function(event) {
            event.preventDefault()
            let data = $('#create_form').serialize();   
            console.log(data)
            $.ajax({
                url: url, 
                headers: {
                    'Content-Type' : 'application/json'
                },
                type: "POST", 
                data: data, 
                processData: false, 
                contentType: false, 
                success: function(data, textStatus, jqXHR) {
                    console.log(data)
                }, 
                error: function(data, textStatus, jqXHR) {
                    console.log(data)
                }, 
            })
        })
    })
}

var url = window.location.href
if(window.location.pathname === "/blog/") {
    loadBlogs()
} else if(window.location.pathname.match(/[0-9]/)) {
    const parts = url.split("/")
    const blog_id = parts.pop() || parts.pop()
    blogDetail(`http://127.0.0.1:8000/api/blogs/${blog_id}`)

} else if (window.location.pathname === '/blog/create/') {
    blogCreate('http://127.0.0.1:8000/api/create/')
}

$(document).ready(function() {
    $(".divvy").mouseenter(function(){
        $(this).find("a").css("color", "gray")
        $(this).find(".date_time").css("color", "black").removeClass("text-muted")
      });
    
    $(".divvy").mouseleave(function(){
        $(this).find("a").css("color", "black")
        $(this).find(".date_time").css("color", "black").addClass("text-muted")
    });

    $(".divvy").click(function () {
        blogLink = $(this).find("a").attr('href')
        window.location.href = blogLink 
    })

});

