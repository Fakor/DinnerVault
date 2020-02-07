function create_header(path) {
    let header=document.createElement("div")
    header.setAttribute("class", "header");
    img = document.createElement("img");
    img.setAttribute("src", path);
    header.appendChild(img)
    document.body.appendChild(header);
}

function create_top_button(text, path){
    let button=document.createElement("button");
    button.setAttribute("class", "top");
    button.onclick= function() {location.href=path;};
    button.setAttribute("type", "button");
    button.innerHTML = text;
    document.body.appendChild(button);
}
