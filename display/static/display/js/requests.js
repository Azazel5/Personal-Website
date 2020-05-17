function loadblogs() {
    fetch('http://127.0.0.1:8000/api/blogs/')
    .then(response => response.json())
    .then(data => {
        data.forEach(element => {
            document.getElementById("blog_list").innerHTML += 
            `${element.title} | ${element.date_posted} 
             ${element.content}
            ` + '<br />'
        });
    }); 
}

loadblogs()