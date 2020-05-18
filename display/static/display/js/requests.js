const loadBlogs = async() => {
    const response = await fetch('http://127.0.0.1:8000/api/blogs/')
    .then(response => response.json())
    .then(data => {
        for(let i = 0; i < data.length; i++) {
            document.getElementById(`image${i+1}`).setAttribute('src', data[i].image)
            document.getElementById(`blog_list${i+1}`).innerHTML += 
            `${data[i].date_posted} 
            ` + '<br />'
            document.getElementById(`heading${i+1}`).innerHTML = data[i].title
        }
    }); 

    return response
}

const blogDetail = async(url) => {
    const response = await fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log(data.image)
        document.getElementById("image").setAttribute('src', data.image)
        document.getElementById("content_holder").innerHTML += 
        `<h3 class='mt-5'>${data.title}</h1
        <p class='mt-2'>${data.content}</p>
        `
    });

    return response 
}

var url = window.location.href
if(window.location.pathname == "/blog/") {
    loadBlogs()
} else if(url.match(/[0-9]/)) {
    const parts = url.split("/")
    const blog_id = parts.pop() || parts.pop()
    blogDetail(`http://127.0.0.1:8000/api/blogs/${blog_id}`)
} else {
    console.log("NOPE NOPE")
}

